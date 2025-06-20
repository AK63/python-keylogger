# 🔐 Python Keylogger

A simple keylogger built in Python that records every keystroke with timestamps. The log is saved locally in a text file. This project is for **educational and ethical** purposes only.

---

## 📌 Features

- 🕒 Logs **every key pressed** with a timestamp
- ⛔ Press `ESC` to safely stop the logger
- 📝 Saves logs to `log.txt` file
- 🧊 Final version converted to a **Windows `.exe`** using PyInstaller

---

## 📂 Folder Structure

keylogger/
├── keylogger.py # Main script
├── log.txt # Auto-generated log file (excluded from Git)
├── README.md # Project description
├── .gitignore # Ignores dist/, build/, pycache/

---

 How It Works

- Uses the `pynput` library to monitor keypresses
- Each key is written to `log.txt` with a timestamp
- Pressing `ESC` stops the logger
- Can be converted to a `.exe` file using PyInstaller for Windows systems

---

How to Run (From Python)

```bash
pip install pynput
python keylogger.py
```
How to Build the Executable (.exe)
```
pip install pyinstaller
pyinstaller --onefile --noconsole --hidden-import=pynput keylogger.py
```
Author
Khan Affan 
