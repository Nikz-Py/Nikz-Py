#!/usr/bin/env python3
"""
Telegram Bot with Multiple Features
Created by: Nikz-Py
"""

import os
import logging
import random
import asyncio
import requests
from datetime import datetime
from typing import Final

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler,
    filters, 
    ContextTypes
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot configuration
TOKEN: Final = os.getenv('BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME', '@your_bot_username')

# Sample data
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
]

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems!"
]

class TelegramBot:
    def __init__(self):
        self.user_data = {}
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command - welcome message"""
        user = update.effective_user
        welcome_message = f"""
🤖 Welcome {user.first_name}! 

I'm a multi-purpose Telegram bot created by Nikz-Py.

📋 **Available Commands:**
/help - Show all commands
/quote - Get a random inspirational quote
/joke - Get a random joke
/weather <city> - Get weather information
/reverse <text> - Reverse your text
/count <text> - Count words in text
/dice - Roll a dice
/coin - Flip a coin
/about - About this bot
/features - See all features

Let's get started! 🚀
        """
        
        keyboard = [
            [InlineKeyboardButton("📋 Help", callback_data='help')],
            [InlineKeyboardButton("🎲 Games", callback_data='games')],
            [InlineKeyboardButton("🌟 Quote", callback_data='quote')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(welcome_message, reply_markup=reply_markup)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command - show all available commands"""
        help_message = """
📋 **Bot Commands:**

🎯 **Basic Commands:**
/start - Start the bot
/help - Show this help message
/about - About this bot

🎮 **Fun Commands:**
/quote - Random inspirational quote
/joke - Random joke
/dice - Roll a dice (1-6)
/coin - Flip a coin

🛠️ **Utility Commands:**
/weather <city> - Weather info
/reverse <text> - Reverse text
/count <text> - Count words
/time - Current time

🎲 **Games:**
/guess - Number guessing game

💡 **Features:**
• Interactive keyboard buttons
• Weather information
• Text utilities
• Random content
• Simple games

Created with ❤️ by Nikz-Py
        """
        await update.message.reply_text(help_message)
    
    async def quote_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a random quote"""
        quote = random.choice(QUOTES)
        await update.message.reply_text(f"💭 *{quote}*", parse_mode='Markdown')
    
    async def joke_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a random joke"""
        joke = random.choice(JOKES)
        await update.message.reply_text(f"😄 {joke}")
    
    async def weather_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Get weather information for a city"""
        if not context.args:
            await update.message.reply_text("Please provide a city name!\nExample: /weather London")
            return
        
        city = ' '.join(context.args)
        try:
            # Using a free weather API (OpenWeatherMap)
            # Note: You'll need to get a free API key from openweathermap.org
            api_key = os.getenv('WEATHER_API_KEY')
            if not api_key:
                await update.message.reply_text("⚠️ Weather service not configured. Contact the bot admin.")
                return
            
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if response.status_code == 200:
                weather = data['weather'][0]['description'].title()
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                
                weather_message = f"""
🌤️ **Weather in {city.title()}:**

🌡️ Temperature: {temp}°C
🤒 Feels like: {feels_like}°C
💧 Humidity: {humidity}%
☁️ Conditions: {weather}
                """
                await update.message.reply_text(weather_message)
            else:
                await update.message.reply_text(f"❌ Could not find weather data for '{city}'. Please check the city name.")
        
        except Exception as e:
            logger.error(f"Weather API error: {e}")
            await update.message.reply_text("❌ Weather service temporarily unavailable.")
    
    async def reverse_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Reverse the provided text"""
        if not context.args:
            await update.message.reply_text("Please provide text to reverse!\nExample: /reverse Hello World")
            return
        
        text = ' '.join(context.args)
        reversed_text = text[::-1]
        await update.message.reply_text(f"🔄 Reversed: `{reversed_text}`", parse_mode='Markdown')
    
    async def count_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Count words in the provided text"""
        if not context.args:
            await update.message.reply_text("Please provide text to count!\nExample: /count Hello beautiful world")
            return
        
        text = ' '.join(context.args)
        word_count = len(text.split())
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        
        count_message = f"""
📊 **Text Statistics:**
📝 Text: {text}
🔢 Words: {word_count}
📏 Characters: {char_count}
📐 Characters (no spaces): {char_count_no_spaces}
        """
        await update.message.reply_text(count_message)
    
    async def dice_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Roll a dice"""
        result = random.randint(1, 6)
        dice_emoji = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"][result - 1]
        await update.message.reply_text(f"🎲 You rolled: {dice_emoji} ({result})")
    
    async def coin_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Flip a coin"""
        result = random.choice(["Heads", "Tails"])
        emoji = "👑" if result == "Heads" else "🦅"
        await update.message.reply_text(f"🪙 Coin flip result: {emoji} {result}!")
    
    async def time_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Get current time"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await update.message.reply_text(f"🕐 Current time: {current_time}")
    
    async def guess_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start a number guessing game"""
        user_id = update.effective_user.id
        number = random.randint(1, 100)
        self.user_data[user_id] = {'game': 'guess', 'number': number, 'attempts': 0}
        
        await update.message.reply_text(
            "🎯 **Number Guessing Game!**\n\n"
            "I've thought of a number between 1 and 100.\n"
            "Send me your guess! You have unlimited attempts.\n"
            "Type /stopgame to stop playing."
        )
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """About the bot"""
        about_message = """
🤖 **About This Bot**

👨‍💻 **Developer:** Nikz-Py
🛠️ **Built with:** Python & python-telegram-bot
📅 **Created:** 2024
🔗 **GitHub:** https://github.com/Nikz-Py

**Features:**
• Multi-purpose functionality
• Interactive commands
• Weather information
• Text utilities
• Simple games
• Clean, modern interface

**Tech Stack:**
🐍 Python
📱 Telegram Bot API
☁️ Async/Await
🌐 REST APIs

Thanks for using this bot! 🙏
        """
        await update.message.reply_text(about_message)
    
    async def features_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show bot features"""
        keyboard = [
            [InlineKeyboardButton("🌤️ Weather", callback_data='weather_demo')],
            [InlineKeyboardButton("🎲 Games", callback_data='games_demo')],
            [InlineKeyboardButton("🛠️ Utilities", callback_data='utils_demo')],
            [InlineKeyboardButton("💬 Fun", callback_data='fun_demo')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🌟 **Bot Features:**\n\nChoose a category to learn more:",
            reply_markup=reply_markup
        )
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard button presses"""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'help':
            await self.help_command(update, context)
        elif query.data == 'quote':
            await self.quote_command(update, context)
        elif query.data == 'games':
            games_message = """
🎮 **Available Games:**

🎲 /dice - Roll a dice
🪙 /coin - Flip a coin
🎯 /guess - Number guessing game

More games coming soon!
            """
            await query.edit_message_text(games_message)
        elif query.data == 'weather_demo':
            await query.edit_message_text(
                "🌤️ **Weather Feature:**\n\n"
                "Get real-time weather information for any city!\n\n"
                "Usage: /weather <city name>\n"
                "Example: /weather London"
            )
        elif query.data == 'games_demo':
            await query.edit_message_text(
                "🎲 **Games Feature:**\n\n"
                "• Roll dice\n"
                "• Flip coins\n"
                "• Number guessing\n"
                "• More coming soon!\n\n"
                "Try: /dice or /coin"
            )
        elif query.data == 'utils_demo':
            await query.edit_message_text(
                "🛠️ **Utility Features:**\n\n"
                "• Text reversal\n"
                "• Word counting\n"
                "• Current time\n"
                "• More utilities planned!\n\n"
                "Try: /reverse Hello World"
            )
        elif query.data == 'fun_demo':
            await query.edit_message_text(
                "💬 **Fun Features:**\n\n"
                "• Random quotes\n"
                "• Jokes collection\n"
                "• Interactive keyboards\n"
                "• Engaging responses\n\n"
                "Try: /quote or /joke"
            )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        user_id = update.effective_user.id
        text = update.message.text.lower()
        
        # Handle guessing game
        if user_id in self.user_data and self.user_data[user_id].get('game') == 'guess':
            try:
                guess = int(text)
                game_data = self.user_data[user_id]
                game_data['attempts'] += 1
                target = game_data['number']
                
                if guess == target:
                    await update.message.reply_text(
                        f"🎉 Congratulations! You guessed it!\n"
                        f"The number was {target}.\n"
                        f"It took you {game_data['attempts']} attempts!"
                    )
                    del self.user_data[user_id]
                elif guess < target:
                    await update.message.reply_text(f"📈 Too low! Try a higher number.")
                else:
                    await update.message.reply_text(f"📉 Too high! Try a lower number.")
                return
            except ValueError:
                await update.message.reply_text("Please enter a valid number!")
                return
        
        # Handle other messages
        if 'hello' in text or 'hi' in text:
            await update.message.reply_text(f"Hello {update.effective_user.first_name}! 👋")
        elif 'how are you' in text:
            await update.message.reply_text("I'm doing great! Thanks for asking. How can I help you today?")
        elif 'thanks' in text or 'thank you' in text:
            await update.message.reply_text("You're welcome! 😊")
        else:
            await update.message.reply_text(
                "I'm not sure how to respond to that. Try /help to see what I can do!"
            )
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Update {update} caused error {context.error}")

def main():
    """Main function to run the bot"""
    if not TOKEN:
        logger.error("BOT_TOKEN not found in environment variables!")
        return
    
    # Create application
    app = Application.builder().token(TOKEN).build()
    bot = TelegramBot()
    
    # Add handlers
    app.add_handler(CommandHandler("start", bot.start_command))
    app.add_handler(CommandHandler("help", bot.help_command))
    app.add_handler(CommandHandler("quote", bot.quote_command))
    app.add_handler(CommandHandler("joke", bot.joke_command))
    app.add_handler(CommandHandler("weather", bot.weather_command))
    app.add_handler(CommandHandler("reverse", bot.reverse_command))
    app.add_handler(CommandHandler("count", bot.count_command))
    app.add_handler(CommandHandler("dice", bot.dice_command))
    app.add_handler(CommandHandler("coin", bot.coin_command))
    app.add_handler(CommandHandler("time", bot.time_command))
    app.add_handler(CommandHandler("guess", bot.guess_command))
    app.add_handler(CommandHandler("about", bot.about_command))
    app.add_handler(CommandHandler("features", bot.features_command))
    
    # Add callback query handler for inline keyboards
    app.add_handler(CallbackQueryHandler(bot.button_callback))
    
    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    
    # Add error handler
    app.add_error_handler(bot.error_handler)
    
    # Start the bot
    logger.info("Starting bot...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()