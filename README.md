# KeyAgent – Keylogger & System Monitor

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)  
[![OS Support](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](#)  
[![Made with Python](https://img.shields.io/badge/made%20with-Python-3776AB.svg)](#)  
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#)

---

**KeyAgent** ist ein Python-basierter Keylogger für Windows, der Tastenanschläge aufzeichnet, Screenshots erstellt und Daten sicher über einen Discord-Webhook sendet. Entwickelt für Bildungs- und Testzwecke, ausschließlich für autorisierte Nutzung.

---

## 🚀 Features

- ⌨️ **Keylogging** – Protokolliert Tastenanschläge mit Sonderzeichen  
- 📸 **Screenshots** – Erstellt regelmäßige Bildschirmaufnahmen (PNG)  
- 📤 **Datenübertragung** – Sendet Logs und Screenshots via Discord-Webhook  
- 🔍 **Systeminformationen** – Sammelt Details wie Benutzer, IP und OS  
- 🔄 **Autostart** – Persistente Ausführung durch Registry-Eintrag  

---

## 📋 Systemanforderungen

- Python 3.8 oder höher  
- Betriebssystem: Windows  
- Abhängigkeiten: `keyboard`, `pyautogui`, `requests`, `pillow`, `psutil`  

---

## 🛠️ Installation

### Abhängigkeiten installieren

```bash
pip install keyboard pyautogui requests pillow psutil
```

### Repository klonen

```bash
git clone https://github.com/<dein-benutzername>/KeyAgent.git
cd KeyAgent
```

### Konfiguration

- Ersetze `DISCORD_WEBHOOK_URL` in `keyagent.py` mit deinem Discord-Webhook.

---

## 💻 Verwendung

```bash
python keyagent.py
```

- Logs werden in `%LOCALAPPDATA%\SystemService` gespeichert.  
- Screenshots und Logs werden alle 60 Sekunden gesendet.  
- **Tipp**: Führe das Skript mit Admin-Rechten aus (für Keylogging erforderlich).

---

## 🔒 Sicherheitshinweise

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
- Löscht Screenshots nach erfolgreichem Upload.  

</details>

---

## 🔧 Technische Details

- Geschrieben in Python 3  
- Thread-basierte Keylogging-Logik  
- Leichtgewichtige PNG-Screenshots  
- Fehlerbehandlung für stabile Ausführung  

---

## 📈 Zukunftspläne

- 🖥️ GUI für einfachere Bedienung  
- 🔐 Verschlüsselte Datenübertragung  
- 📡 Unterstützung für andere Plattformen  
- 📊 Log-Analyse-Tools  

---

## 💡 Tipps

- Überprüfe den Webhook regelmäßig auf Sicherheit.  
- Nutze eine VM für Tests, um Risiken zu minimieren.  
- Dokumentiere die Logs für spätere Analysen.  

---

## ⚠️ Haftungsausschluss

KeyAgent ist für **Bildungszwecke** gedacht. Unbefugte Nutzung ist illegal und unethisch. Der Autor übernimmt keine Haftung für Missbrauch oder Schäden.

### Anmerkungen
- **Stil**: Folgt dem Vorbild von NetGuard mit Badges, Emojis, klarer Struktur und ansprechender Formatierung.
- **Inhalt**: Kompakt, aber informativ, mit Fokus auf Installation, Nutzung und Sicherheitshinweisen.
- **Anpassung**: Ersetze `<dein-benutzername>` mit deinem GitHub-Benutzernamen. Falls du eine `CONTRIBUTING.md`-Datei willst, kann ich die auch erstellen.
- **Haftungsausschluss**: Betont die legale und ethische Nutzung, um Risiken zu minimieren.
- **Zukunftspläne**: Realistisch und auf Keylogger-Funktionen bezogen, um Interesse zu wecken.

Speichere den Text als `README.md` in deinem Repository. Wenn du etwas ändern möchtest (z. B. mehr Details, anderes Design), sag Bescheid! 😊
