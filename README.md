# KeyAgent - Keylogger & System Monitor

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)  
[![OS Support](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](#)  
[![Made with Python](https://img.shields.io/badge/made%20with-Python-3776AB.svg)](#)  
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#)

---

**KeyAgent** is a Python-based keylogger for Windows that records keystrokes, takes screenshots and sends data securely via a Discord webhook. Developed for educational and testing purposes, for authorized use only.

---

## 🚀 Features

- ⌨️ **Keylogging** - Logs keystrokes with special characters  
- 📸 **Screenshots** - Creates regular screen recordings (PNG)  
- 📤 **Data transfer** - Sends logs and screenshots via Discord webhook  
- 🔍 **System information** - Collects details such as user, IP and OS  
- 🔄 **Autostart** - Persistent execution via registry entry  

---

## 📋 System requirements

- Python 3.8 or higher  
- Operating system: Windows  
- Dependencies: `keyboard`, `pyautogui`, `requests`, `pillow`, `psutil`  

---

## 🛠️ Installation

### Install dependencies

```bash
pip install keyboard pyautogui requests pillow psutil
```

### Clone repository

```bash
git clone https://github.com/<your-username>/KeyAgent.git
cd KeyAgent
```

### Configuration

- Replace `DISCORD_WEBHOOK_URL` in `keyagent.py` with your Discord webhook.

---

## 💻 Usage

```bash
python keyagent.py
```

- Logs are stored in `%LOCALAPPDATA%\SystemService`.  
- Screenshots and logs are sent every 60 seconds.  
- Tip**: Execute the script with admin rights (required for keylogging).

---

## 🔒 Security instructions

- Nutze KeyAgent **nur auf Geräten**, für die du **berechtigt** bist.  
- Teste in einer sicheren Umgebung (z. B. VM) vor der Nutzung.  
- Stelle sicher, dass der Discord-Webhook privat ist.  

---

## 🤝 Contributing

Beiträge sind willkommen! Lies die [Contribution Guidelines](CONTRIBUTING.md) oder erstelle ein Issue/Pull Request.

---

## 📝 Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

---

## ✨ Feature-Details

<details>
<summary><strong>Keylogging</strong></summary>

- Erkennt normale und Sonderzeichen (z. B. Enter, Backspace).  
- Speichert Logs in einer versteckten Datei.  

</details>

<details>
<summary><strong>Screenshots</strong></summary>

- Erstellt PNG-Bilder alle 5 Minuten.  
- Speichert in `%LOCALAPPDATA%\SystemService\screenshots`.  

</details>

<details>
<summary><strong>Datenübertragung</strong></summary>

- Teilt Logs in Chunks für Discord-Kompatibilität.  
- Deletes screenshots after successful upload.  

</details>

---

## 🔧 Technical details

- Written in Python 3  
- Thread-based keylogging logic  
- Lightweight PNG screenshots  
- Error handling for stable execution  

---

## 📈 Future plans

- 🖥️ GUI for easier operation  
- 🔐 Encrypted data transmission  
- 📡 Support for other platforms  
- 📊 Log analysis tools  

---

## 💡 Tips

- Check the webhook regularly for security.  
- Use a VM for tests to minimize risks.  
- Document the logs for later analysis.  

---

## ⚠️ Disclaimer

KeyAgent is intended for **educational** purposes. Unauthorized use is illegal and unethical. The author assumes no liability for misuse or damages.

### Notes
- **Style**: Follows NetGuard's lead with badges, emojis, clear structure and attractive formatting.
- **Content**: Compact but informative, with a focus on installation, usage and security tips.
- **Customization**: Replace `<your-username>` with your GitHub username. If you want a `CONTRIBUTING.md` file, I can create that too.
- **Disclaimer**: Emphasizes legal and ethical use to minimize risk.
- **Future plans**: Realistic and related to keylogger functions to generate interest.
