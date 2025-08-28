
# 🤖 Telegram Bot

A feature-rich Telegram bot built with Python using the `python-telegram-bot` package.

## 📋 Features

### 🎯 Core Commands
- `/start` - Welcome message with interactive buttons
- `/help` - Complete command list
- `/about` - Bot information

### 🎮 Entertainment
- `/quote` - Random inspirational quotes
- `/joke` - Random jokes
- `/dice` - Roll a dice (1-6)
- `/coin` - Flip a coin
- `/guess` - Number guessing game

### 🛠️ Utilities
- `/weather <city>` - Real-time weather information
- `/reverse <text>` - Reverse any text
- `/count <text>` - Count words and characters
- `/time` - Current date and time

### 💡 Interactive Features
- Inline keyboard buttons
- Callback handling
- Game state management
- Error handling with user-friendly messages

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- A Telegram Bot Token (get from [@BotFather](https://t.me/BotFather))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd telegram-bot
   ```

2. **Set up environment**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure your bot**
   - Edit `.env` file and add your bot token:
   ```
   BOT_TOKEN=your_actual_bot_token_here
   ```

4. **Run the bot**
   ```bash
   # Simple start
   python telegram_bot.py
   
   # Or use the startup script (recommended)
   python start_bot.py
   ```

## 🔧 Configuration

### Required Settings
- `BOT_TOKEN`: Get from [@BotFather](https://t.me/BotFather) on Telegram

### Optional Settings
- `BOT_USERNAME`: Your bot's username (with @)
- `WEATHER_API_KEY`: Free API key from [OpenWeatherMap](https://openweathermap.org/api)

## 📖 Getting a Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the token and add it to your `.env` file

## 🌤️ Weather Feature Setup (Optional)

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Get your API key
4. Add it to your `.env` file as `WEATHER_API_KEY`

## 📱 Bot Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Start the bot | `/start` |
| `/help` | Show all commands | `/help` |
| `/quote` | Random quote | `/quote` |
| `/joke` | Random joke | `/joke` |
| `/weather` | Weather info | `/weather London` |
| `/reverse` | Reverse text | `/reverse Hello World` |
| `/count` | Count words | `/count Hello beautiful world` |
| `/dice` | Roll dice | `/dice` |
| `/coin` | Flip coin | `/coin` |
| `/time` | Current time | `/time` |
| `/guess` | Number game | `/guess` |
| `/about` | Bot info | `/about` |
| `/features` | Feature demo | `/features` |

## 🏗️ Project Structure

```
telegram-bot/
├── telegram_bot.py      # Main bot application
├── start_bot.py         # Startup script with checks
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── .env               # Your configuration (create this)
└── README.md          # This file
```

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **Bot Framework**: python-telegram-bot 20.7
- **APIs**: OpenWeatherMap (optional)
- **Environment**: python-dotenv
- **HTTP Requests**: requests, aiohttp

## 🔧 Development

### Adding New Commands

1. Create a new method in the `TelegramBot` class:
   ```python
   async def your_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
       """Your command description"""
       await update.message.reply_text("Your response")
   ```

2. Register the command in the `main()` function:
   ```python
   app.add_handler(CommandHandler("yourcommand", bot.your_command))
   ```

### Adding Inline Keyboards

```python
keyboard = [
    [InlineKeyboardButton("Button Text", callback_data='callback_id')]
]
reply_markup = InlineKeyboardMarkup(keyboard)
await update.message.reply_text("Message", reply_markup=reply_markup)
```

## 📝 Error Handling

The bot includes comprehensive error handling:
- Graceful API failures
- User input validation
- Network timeout handling
- Logging for debugging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## � License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

Created by **Nikz-Py**

### 🌐 Connect
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/)

### 💻 Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

---

**⭐ Star this repository if you found it helpful!**
