### KeyAgent

[

](LICENSE)
[

](https://www.python.org/downloads/)
[

](#)
[

](https://www.python.org/)
[

](CONTRIBUTING.md)

A lightweight, educational Windows keylogger and system monitoring tool built with Python.

## 📋 Overview

KeyAgent is a Python-based monitoring tool for Windows that records keystrokes, captures screenshots, and transmits data via Discord webhooks. This project is designed for **educational purposes** and **authorized system monitoring only**.





## ✨ Key Features

- **Keystroke Logging** - Captures all keyboard input including special keys
- **Screenshot Capture** - Takes periodic screenshots of the system
- **Discord Integration** - Securely sends collected data via webhooks
- **System Information** - Gathers hardware, network, and user details
- **Persistence** - Optional Windows registry integration for automatic startup


## 🚀 Quick Start

### Prerequisites

- Windows operating system
- Python 3.8 or higher
- Required packages: `keyboard`, `pyautogui`, `requests`, `pillow`, `psutil`


### Installation

1. Clone the repository:

```shellscript
git clone https://github.com/yourusername/KeyAgent.git
cd KeyAgent
```


2. Install dependencies:

```shellscript
pip install -r requirements.txt
```


3. Configure your Discord webhook:

1. Open `config.py`
2. Replace `DISCORD_WEBHOOK_URL` with your webhook URL





### Usage

Run the main script with administrator privileges:

```shellscript
python keyagent.py
```

## 🔧 Configuration Options

| Setting | Description | Default
|-----|-----|-----
| `SCREENSHOT_INTERVAL` | Time between screenshots (seconds) | 300
| `LOG_INTERVAL` | Time between log transmissions (seconds) | 60
| `ENABLE_AUTOSTART` | Add to Windows startup | False
| `LOG_DIRECTORY` | Local storage location | %LOCALAPPDATA%\SystemService


## 📚 Documentation

### Data Collection

KeyAgent collects the following information:

- Keystrokes (including special keys)
- Periodic screenshots
- System information (username, hostname, IP address)
- Active window titles


### Data Storage

- Logs are stored locally in `%LOCALAPPDATA%\SystemService`
- Screenshots are saved as PNG files in the `screenshots` subdirectory
- All data is transmitted via Discord webhook at configurable intervals


## 🛡️ Legal & Ethical Use

**IMPORTANT**: This software must only be used on systems you own or have explicit permission to monitor. Unauthorized use of KeyAgent may violate:

- Computer Fraud and Abuse Act
- Electronic Communications Privacy Act
- Various state and international privacy laws


The developers assume no liability for misuse or damages resulting from the use of this software.

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [PyLogger](https://github.com/topics/python-keylogger) - Similar Python-based keyloggers
- [System Monitor](https://github.com/topics/system-monitoring) - System monitoring tools
- [Discord Webhooks](https://github.com/topics/discord-webhook) - Discord webhook integrations


---

`<sub>`⚠️ For educational purposes only. Use responsibly and ethically. ⚠️`</sub>`
