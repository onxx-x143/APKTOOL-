# 🔥 APK Signer + Protector Tool v3.1

**Termux‑ready Python script** that signs any APK with **V1, V2 & V3** signatures, adds 
## ❇️Termux install 
```
git clone https://github.com/onxx-x143/APKTOOL-.git
cd APKTOOL


**code‑hiding protection**, and lets you save the output to **any folder** (including `/sdcard/Download` for MT Manager).  
Automatically installs all dependencies, displays a **stunning red ASCII banner**, and redirects to the creator’s GitHub profile on startup.

---

#insta
URL https://www.instagram.com/_insrnx_?igsh=MTg0bTVyZTVqOXNhbQ==

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
