#!/usr/bin/env python3
"""
Telegram Bot Startup Script
This script checks the environment and starts the bot
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if environment is properly configured"""
    print("🔍 Checking environment...")
    
    # Check if .env file exists
    if not Path('.env').exists():
        print("❌ .env file not found!")
        print("📝 Please copy .env.example to .env and configure your bot token")
        print("   cp .env.example .env")
        return False
    
    # Load and check environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token or bot_token == 'your_bot_token_here':
        print("❌ BOT_TOKEN not configured!")
        print("📝 Please set your bot token in the .env file")
        print("   Get your token from @BotFather on Telegram")
        return False
    
    print("✅ Environment configured correctly!")
    return True

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    os.system("pip install -r requirements.txt")

def main():
    """Main startup function"""
    print("🤖 Telegram Bot Startup")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required")
        sys.exit(1)
    
    # Install dependencies
    install_dependencies()
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Start the bot
    print("🚀 Starting bot...")
    from telegram_bot import main as bot_main
    bot_main()

if __name__ == '__main__':
    main()