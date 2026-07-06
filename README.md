# 🔥 APK Signer + Protector Tool v3.1

**Termux‑ready Python script** that signs any APK with **V1, V2 & V3** signatures, adds 
## ❇️Termux install 
```
git clone https://github.com/onxx-x143/APKTOOL-.git
cd APKTOOL
chmod +x nxz.py
python3 nxz.py
```

## 💥Direct install
```
curl -L -o nxz.py https://raw.githubusercontent.com/onxx-x143/APKTOOL/main/nxz.py && python nxz.py
```

## Linux 💻
```
sudo apt update sudo apt upgrade 
pip install colorama requests
termux-setup-storage
python3 nxz.py
```
**code‑hiding protection**, and lets you save the output to **any folder** (including `/sdcard/Download` for MT Manager).  
Automatically installs all dependencies, displays a **stunning red ASCII banner**, and redirects to the creator’s GitHub profile on startup.

---

## Feedback
by onxx-x143 ❇️
[![Instagram](https://img.shields.io/badge/Instagram-Follow%20Now-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_insrnx_)

[![YouTube](https://img.shields.io/badge/YouTube-Subscribe%20Now-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@hari.x145)

[![Telegram](https://img.shields.io/badge/Telegram-Join%20Now-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/harijadhavai)

## ✨ Features

- ✅ **Full V1+V2+V3 signing** using `apksigner`
- ✅ **Advanced protection** (APK decoding via `apktool`, removal of `debuggable` flag, injection of dummy Smali class, rebuild & re‑sign)
- ✅ **Fallback protection** if advanced method fails – injects a dummy file and re‑signs
- ✅ **Download APK from any URL** with progress bar
- ✅ **Save to any folder** – local, external, or `/sdcard/Download/` (MT Manager)
- ✅ **Automatic dependency installation** for Termux (`java`, `apksigner`, `zipalign`, `apktool`)
- ✅ **GitHub redirect** – opens `https://github.com/onxx-x143` when the tool starts
- ✅ **Clear screen** on launch
- ✅ **All‑red custom ASCII banner** (your design)

---

## 📦 Requirements

- **Termux** (Android)
- Python 3.8+
- Internet connection (for dependency installation and APK downloads)

---

## 🚀 Installation & Usage

### 1. Update Termux and install Python

```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install colorama requests
termux-setup-storage
