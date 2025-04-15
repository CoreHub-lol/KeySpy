### KeyAgent - Keylogger & System Monitor

[

](LICENSE)[

](https://www.python.org/downloads/)[

](#)[

](#)[

](#)

---

**KeyAgent** is a Python-based keylogger for Windows that records keystrokes, takes screenshots, and sends data securely via a Discord webhook. Developed for educational and testing purposes only, for authorized use on systems you own or have permission to monitor.

---

## 🚀 Features

- ⌨️ **Keylogging** - Captures all keystrokes including special characters
- 📸 **Screenshots** - Takes periodic screen captures in PNG format
- 📤 **Data Transfer** - Securely sends logs and screenshots via Discord webhook
- 🔍 **System Information** - Collects user details, IP address, and OS information
- 🔄 **Autostart** - Ensures persistent execution through Windows registry


---

## 📋 System Requirements

- Python 3.8 or higher
- Operating system: Windows
- Dependencies: `keyboard`, `pyautogui`, `requests`, `pillow`, `psutil`


---

## 🛠️ Installation

### Install Dependencies

```shellscript
pip install keyboard pyautogui requests pillow psutil
```

### Clone Repository

```shellscript
git clone https://github.com/<your-username>/KeyAgent.git
cd KeyAgent
```

### Configuration

- Replace `DISCORD_WEBHOOK_URL` in `keyagent.py` with your Discord webhook URL.


---

## 💻 Usage

```shellscript
python keyagent.py
```

- Logs are stored in `%LOCALAPPDATA%\SystemService`.
- Screenshots and logs are sent every 60 seconds.
- **Important**: Execute the script with administrator rights (required for keylogging).


---

## 🔒 Security Instructions

- Use KeyAgent **only on devices** that you **own or have explicit permission** to monitor.
- Test in a secure environment (e.g., virtual machine) before deployment.
- Ensure your Discord webhook is private and secure.


---

## 🤝 Contributing

Contributions are welcome! Please read the [Contribution Guidelines](CONTRIBUTING.md) or create an issue/pull request.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Feature Details

<details>`<summary>``<strong>`Keylogging`</strong>``</summary>`

- Detects standard and special characters (e.g., Enter, Backspace).
- Stores logs in a hidden file for security.


</details><details>`<summary>``<strong>`Screenshots`</strong>``</summary>`

- Creates PNG images every 5 minutes.
- Saves to `%LOCALAPPDATA%\SystemService\screenshots`.


</details><details>`<summary>``<strong>`Data Transfer`</strong>``</summary>`

- Splits logs into chunks for Discord compatibility.
- Deletes screenshots after successful upload.


</details>---

## 🔧 Technical Details

- Written in Python 3
- Thread-based keylogging logic
- Lightweight PNG screenshots
- Error handling for stable execution


---

## 📈 Future Plans

- 🖥️ GUI for easier operation
- 🔐 Encrypted data transmission
- 📡 Support for additional platforms
- 📊 Log analysis tools


---

## 💡 Tips

- Check your webhook regularly for security.
- Use a virtual machine for testing to minimize risks.
- Document the logs for later analysis.


---

## ⚠️ Disclaimer

KeyAgent is intended for **educational and authorized monitoring purposes only**. Unauthorized use is illegal and unethical. The author assumes no liability for misuse or damages resulting from the use of this software.

Using keyloggers without consent is illegal in most jurisdictions and violates privacy laws. Always ensure you have proper authorization before monitoring any system.

---

## 🔗 Related Resources

- [Python Documentation](https://docs.python.org/3/)
- [Windows Registry Documentation](https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry)
- [Discord Webhook API](https://discord.com/developers/docs/resources/webhook)
