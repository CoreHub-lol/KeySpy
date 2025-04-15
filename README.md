

# 🕵️‍♂️ KeyAgent

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](#)
[![Python Org](https://img.shields.io/badge/Built%20with-Python-blue.svg)](https://www.python.org/)

> A lightweight, educational Windows keylogger and system monitoring tool built with Python.

---

## 📋 Overview

**KeyAgent** is a Python-based monitoring tool for Windows that records keystrokes, captures screenshots, and transmits data via Discord webhooks. This project is intended for **educational** and **authorized system monitoring only**.

---

## ✨ Features

- ⌨️ **Keystroke Logging** – Captures all keyboard input including special keys  
- 🖼️ **Screenshot Capture** – Takes periodic screenshots of the system  
- 📡 **Discord Integration** – Securely sends collected data via webhooks  
- 🧠 **System Information** – Gathers hardware, network, and user details  
- 🔁 **Persistence** – Optional startup via Windows Registry  

---

## 🚀 Quick Start

### ✅ Prerequisites

- Windows OS
- Python 3.8+
- Required packages:  
  `keyboard`, `pyautogui`, `requests`, `pillow`, `psutil`

### 🛠 Installation

```bash
git clone https://github.com/yourusername/KeyAgent.git
cd KeyAgent
pip install -r requirements.txt
```

### ⚙️ Configuration

1. Open `config.py`  
2. Replace the `DISCORD_WEBHOOK_URL` with your actual Discord webhook URL  

### ▶️ Run

```bash
python keyagent.py
```
> 🔐 Run with **administrator privileges** for full functionality.

---

## 🔧 Configuration Options

| Setting               | Description                                  | Default                             |
|-----------------------|----------------------------------------------|-------------------------------------|
| `SCREENSHOT_INTERVAL` | Time between screenshots (in seconds)        | `300`                               |
| `LOG_INTERVAL`        | Time between log transmissions (in seconds)  | `60`                                |
| `ENABLE_AUTOSTART`    | Add to Windows startup (True/False)          | `False`                             |
| `LOG_DIRECTORY`       | Local storage location for logs              | `%LOCALAPPDATA%\SystemService`      |

---

## 📚 Documentation

### 📥 Data Collection

- Keystrokes (all keys incl. special)
- Periodic screenshots
- System details (user, hostname, IP)
- Active window titles

### 💾 Data Storage

- Local logs: `%LOCALAPPDATA%\SystemService`
- Screenshots: `screenshots/` folder (PNG format)
- Webhook: Discord integration for log delivery

---

## 🛡️ Legal & Ethical Use

> ⚠️ This software **must only be used** on devices you own or have **explicit permission** to monitor.

Misuse may violate:

- U.S. Computer Fraud and Abuse Act  
- Electronic Communications Privacy Act  
- State & international privacy laws  

**The developers are not liable** for any misuse or resulting damages.

---

## 🤝 Contributing

Contributions are always welcome!

1. Fork the repo  
2. Create a feature branch:  
   `git checkout -b feature/amazing-feature`  
3. Commit your changes:  
   `git commit -m 'Add amazing feature'`  
4. Push to GitHub:  
   `git push origin feature/amazing-feature`  
5. Open a Pull Request 🎉  

Check the [Contributing Guidelines](CONTRIBUTING.md) for more info.

---

## 📝 License

Licensed under the MIT License. See the [LICENSE](LICENSE) file.

---

## 🔗 Related Projects

- [PyLogger](https://github.com/topics/python-keylogger) – Python keyloggers  
- [System Monitor](https://github.com/topics/system-monitoring) – Monitoring tools  
- [Discord Webhooks](https://github.com/topics/discord-webhook) – Webhook integrations  

---

> ⚠️ **For educational purposes only. Use responsibly and ethically.**

---

Let me know if you want a dark theme badge version or want this formatted into a `README.md` file directly.
