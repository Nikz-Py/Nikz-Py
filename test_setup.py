#!/usr/bin/env python3
"""
Test Script for Telegram Bot Setup
This script verifies that all dependencies and configuration are correct
"""

import sys
import os
from pathlib import Path

def test_python_version():
    """Test Python version"""
    print("🐍 Testing Python version...")
    if sys.version_info >= (3, 7):
        print(f"   ✅ Python {sys.version.split()[0]} (OK)")
        return True
    else:
        print(f"   ❌ Python {sys.version.split()[0]} (Need 3.7+)")
        return False

def test_dependencies():
    """Test if all required packages are installed"""
    print("\n📦 Testing dependencies...")
    required_packages = [
        'telegram',
        'requests', 
        'dotenv',
        'aiohttp'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} (Missing)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    return True

def test_configuration():
    """Test bot configuration"""
    print("\n⚙️ Testing configuration...")
    
    # Check .env file
    if not Path('.env').exists():
        print("   ❌ .env file not found")
        print("   💡 Copy .env.example to .env and configure")
        return False
    print("   ✅ .env file exists")
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        # Check bot token
        bot_token = os.getenv('BOT_TOKEN')
        if not bot_token:
            print("   ❌ BOT_TOKEN not set")
            return False
        elif bot_token == 'your_bot_token_here':
            print("   ❌ BOT_TOKEN not configured (still default value)")
            return False
        else:
            print("   ✅ BOT_TOKEN configured")
        
        # Check optional settings
        weather_key = os.getenv('WEATHER_API_KEY')
        if weather_key and weather_key != 'your_weather_api_key_here':
            print("   ✅ WEATHER_API_KEY configured")
        else:
            print("   ⚠️ WEATHER_API_KEY not configured (weather commands disabled)")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Configuration error: {e}")
        return False

def test_bot_import():
    """Test if bot module can be imported"""
    print("\n🤖 Testing bot import...")
    try:
        from telegram_bot import TelegramBot
        print("   ✅ Bot module imports successfully")
        return True
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False

def run_tests():
    """Run all tests"""
    print("🧪 Telegram Bot Setup Test")
    print("=" * 40)
    
    tests = [
        test_python_version,
        test_dependencies, 
        test_configuration,
        test_bot_import
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 40)
    if all(results):
        print("🎉 All tests passed! Your bot is ready to run.")
        print("🚀 Start your bot with: python start_bot.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        failed_count = len([r for r in results if not r])
        print(f"   {failed_count}/{len(results)} tests failed")
    
    return all(results)

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)