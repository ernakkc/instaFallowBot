# 🤖 Instagram Follow Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

*Automated Instagram follower bot using Selenium WebDriver*

</div>

---

## ⚠️ IMPORTANT DISCLAIMER

**This tool is provided for educational purposes ONLY.**

- ❌ Using automation on Instagram violates their Terms of Service
- ❌ Your account may be restricted, shadowbanned, or permanently banned
- ❌ Not affiliated with or endorsed by Instagram/Meta
- ⚖️ Users assume all legal and ethical responsibility
- 🔒 Use at your own risk - preferably on test accounts only

**The author is not responsible for any consequences of using this tool.**

---

## 📖 Overview

InstaFollowBot is an automated Instagram bot built with Python and Selenium that sends follow requests to the followers of a target Instagram account. The bot mimics human behavior to avoid detection.

## ✨ Features

- 🎯 **Target User's Followers**: Follow all followers of a specific account
- 🤖 **Automated Following**: Hands-free operation with Selenium
- 🔄 **Smart Delays**: Random delays between actions to appear human
- 📊 **Progress Tracking**: Visual progress indicator
- 🌐 **WebDriver Support**: Chrome WebDriver integration
- 📝 **Logging**: Track bot activities and errors
- ⚙️ **Configurable**: Customize settings easily

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ernakkc/instaFallowBot.git
   cd instaFallowBot
   ```

2. **Install ChromeDriver**:
   - Download from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Match your Chrome version: `chrome://version`
   - Add to PATH or place in project directory

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

### Edit `userInfo.py`

```python
# Your Instagram credentials
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"

# Target account whose followers you want to follow
TARGET_ACCOUNT = "target_username"

# Optional settings
MAX_FOLLOWS = 100  # Maximum follows per session
DELAY_MIN = 2      # Minimum delay between actions (seconds)
DELAY_MAX = 5      # Maximum delay between actions (seconds)
```

### Safety Settings

```python
# Recommended settings to avoid detection
FOLLOW_LIMIT_PER_HOUR = 20
FOLLOW_LIMIT_PER_DAY = 150
USE_RANDOM_DELAYS = True
HEADLESS_MODE = False  # Set True for background operation
```

## 💻 Usage

### Basic Usage

```bash
python app.py
```

### With Custom Settings

```python
from instaFallowBot import InstagramBot

bot = InstagramBot(
    username="your_username",
    password="your_password",
    target="target_account",
    max_follows=50
)

bot.login()
bot.follow_target_followers()
bot.close()
```

## 📊 Features Explained

### Smart Following
- Opens target account's followers list
- Scrolls through followers
- Clicks follow button for each user
- Random delays between follows
- Skips already followed accounts

### Human-like Behavior
```python
import random
import time

# Random delays
delay = random.uniform(DELAY_MIN, DELAY_MAX)
time.sleep(delay)

# Random scroll amounts
scroll_amount = random.randint(200, 400)
```

### Error Handling
- Login failure detection
- Rate limit detection
- Connection error recovery
- Element not found handling

## 🖼️ Screenshots

<div align="center">
  <img src="https://telegra.ph/file/81f475933322d3883dd85.png" alt="Bot Interface" width="600"/>
  <p><em>Bot Interface and Progress Tracking</em></p>
</div>

## 🛡️ Safety Recommendations

### Account Safety
1. **Test Account First**: Use a disposable account initially
2. **Enable 2FA**: Protect your main account with two-factor authentication
3. **Limit Daily Actions**: Stay under Instagram's unofficial limits:
   - Max 150-200 follows per day
   - Max 60 follows per hour
   - Spread actions throughout the day

### Avoiding Detection
- ✅ Use random delays (2-5 seconds minimum)
- ✅ Don't run bot 24/7
- ✅ Vary your actions (follow, like, comment)
- ✅ Monitor for action blocks
- ✅ Stop immediately if you get warnings

### Instagram Limits
- **New accounts** (< 3 months): 20-30 follows/day
- **Regular accounts** (3-6 months): 100-150 follows/day
- **Established accounts** (> 6 months): 150-200 follows/day

## 🐛 Troubleshooting

### ChromeDriver Issues
```bash
# Check Chrome version
chrome://version

# Download matching ChromeDriver
# Add to PATH or use:
driver_path = "/path/to/chromedriver"
```

### Login Failures
- Check credentials in `userInfo.py`
- Disable 2FA or use app-specific password
- Clear browser cookies
- Try logging in manually first

### Element Not Found Errors
- Instagram UI may have changed
- Update selectors in code
- Check internet connection
- Increase wait times

### Rate Limiting
```python
# If you get action blocked:
# 1. Stop the bot immediately
# 2. Wait 24-48 hours
# 3. Reduce daily limits
# 4. Increase delays between actions
```

## 📁 Project Structure

```
instaFallowBot/
├── app.py              # Main bot script
├── userInfo.py         # Configuration file
├── requirements.txt    # Python dependencies
├── chromedriver.exe    # WebDriver (Windows)
├── LICENSE            # MIT License
└── README.md          # This file
```

## 🔧 Advanced Usage

### Headless Mode
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
```

### Proxy Support
```python
options = Options()
options.add_argument('--proxy-server=http://proxy:port')
```

### Custom Filters
```python
# Only follow accounts with specific criteria
def should_follow(user):
    # Check follower count
    # Check bio keywords
    # Check post count
    return True
```

## 📊 Logging

Logs are saved in `bot_logs.txt`:
```
[2026-01-29 14:23:10] Bot started
[2026-01-29 14:23:15] Login successful
[2026-01-29 14:23:20] Followed @user1
[2026-01-29 14:23:25] Followed @user2
...
```

## 🤝 Contributing

Contributions welcome! Please note:
- Maintain ethical automation practices
- Add proper error handling
- Update documentation
- Test thoroughly before submitting

## ⚖️ Legal Notice

This software is provided "as is" without warranty. The author is not responsible for:
- Account suspensions or bans
- Violation of Instagram's Terms of Service
- Misuse of the software
- Legal consequences

Always comply with Instagram's Terms of Service and applicable laws.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Eren Akkoç**
- GitHub: [@ernakkc](https://github.com/ernakkc)
- Email: ern.akkc@gmail.com

## 🔗 Resources

- [Instagram Terms of Service](https://help.instagram.com/581066165581870)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

---

<div align="center">

**⚠️ Use Responsibly and Ethically! 🤝**

*For Educational Purposes Only*

</div>



