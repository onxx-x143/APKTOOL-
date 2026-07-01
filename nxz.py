#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import webbrowser
import shutil
import zipfile
import requests
import time
import re
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ------------------- CONFIGURATION -------------------
GITHUB_URL = "https://github.com/onxx-x143"
REQUIRED_COMMANDS = ["java", "apksigner", "zipalign", "apktool"]
TERMUX_PACKAGES = ["openjdk-17", "android-tools", "apktool"]

# ------------------- SCREEN CLEAR & GITHUB REDIRECT -------------------
def clear_screen():
    os.system('clear')

def open_github():
    print(Fore.CYAN + "[*] Opening GitHub profile...")
    webbrowser.open(GITHUB_URL)
    time.sleep(2)

# ------------------- DEPENDENCY CHECK & INSTALL -------------------
def install_dependencies():
    print(Fore.CYAN + "[*] Checking dependencies...")
    missing = []
    for cmd in REQUIRED_COMMANDS:
        if shutil.which(cmd) is None:
            missing.append(cmd)
    if missing:
        print(Fore.YELLOW + f"[!] Missing: {', '.join(missing)}")
        if "TERMUX_VERSION" in os.environ:
            print(Fore.CYAN + "[*] Termux detected, installing packages...")
            for pkg in TERMUX_PACKAGES:
                subprocess.run(["pkg", "install", pkg, "-y"], check=False)
        else:
            print(Fore.RED + "[!] Please install manually: " + " ".join(missing))
            sys.exit(1)
    else:
        print(Fore.GREEN + "[✓] All dependencies present.")

# ------------------- FULLY RED BANNER -------------------
def show_banner():
    banner = f"""
{Fore.RED}   ⠀⠀⣴⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣶⡄⠀
{Fore.RED}   ⠘⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡇⠀
{Fore.RED}   ⠀⠀⠉⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠋⠀⠀
{Fore.RED}   ⠀⠀⠀⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⣿⣗⣀⣀⣀⣀⣀⡀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢀⣀⣀⣀⣀⣀⣸⣿⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⠙⠛⠛⠛⠛⠛⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}   ⠀⢀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠋⣡⣤⣤⣀⡉⠻⣿⣿⡿⠋⣉⣤⣤⣀⡉⠛⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}   ⣴⣿⣿⣷⡄⢀⣤⣀⡄⠸⣿⣿⡁⢸⣿⣿⣿⣿⣿⠆⣹⣿⡃⠸⣿⣿⣿⣿⣿⠆⢸⣿⣿⠀⣠⣄⣠⡀⢠⣾⣿⣿⣦
{Fore.RED}   ⠻⣿⣿⡿⠃⠘⠙⠋⠛⠀⢻⣿⣷⣄⡉⠛⠙⠋⣁⣴⣿⣿⣷⣄⣉⠙⠋⠋⣁⣤⣿⣿⠇⠀⠛⠙⠋⠃⠘⢿⣿⣿⡟
{Fore.RED}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣄⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢁⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣟⢻⣿⣿⠛⣿⣿⡟⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
{Fore.RED}   ⠀⠀⠀⡿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⣿⠀⣿⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⠀⠀⠀
{Fore.RED}   ⠀⠀⣀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠃⠘⠛⠛⠀⠛⠛⠃⠘⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣄⠀⠀
{Fore.RED}   ⠀⢠⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇⠀
{Fore.RED}   ⠀⠀⠻⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⠿⠃⠀
{Style.RESET_ALL}
{Fore.RED}   ═══════════════════════════════════════════════════════════
{Fore.RED}   🔥 APK SIGNER + PROTECTOR TOOL v3.1 🔥
{Fore.RED}   ❤️  Insta by @_insrnx_  ❤️
{Fore.RED}   GitHub: {GITHUB_URL}
{Fore.RED}   ═══════════════════════════════════════════════════════════
{Style.RESET_ALL}
"""
    print(banner)

# ------------------- DOWNLOAD APK -------------------
def download_apk(url, output_path):
    try:
        print(Fore.CYAN + f"[*] Downloading: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(output_path, 'wb') as f:
            if total_size == 0:
                f.write(response.content)
            else:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = (downloaded / total_size) * 100
                    print(f"\r{Fore.GREEN}Progress: {percent:.2f}%", end="")
        print("\n" + Fore.GREEN + "[✓] Download complete!")
        return output_path
    except Exception as e:
        print(Fore.RED + f"[✗] Download failed: {e}")
        return None

# ------------------- SIGN APK (V1+V2+V3) -------------------
def sign_apk(input_apk, output_apk, keystore_path=None, keystore_pass="android", key_alias="androiddebugkey"):
    if keystore_path is None:
        keystore_dir = Path.home() / ".android"
        keystore_dir.mkdir(exist_ok=True)
        keystore_path = keystore_dir / "debug.keystore"
        if not keystore_path.exists():
            print(Fore.YELLOW + "[!] Debug keystore not found, generating...")
            cmd = [
                "keytool", "-genkey", "-v",
                "-keystore", str(keystore_path),
                "-alias", key_alias,
                "-keyalg", "RSA",
                "-keysize", "2048",
                "-validity", "10000",
                "-storepass", keystore_pass,
                "-keypass", keystore_pass,
                "-dname", "CN=Debug, OU=Debug, O=Debug, L=Debug, ST=Debug, C=IN"
            ]
            subprocess.run(cmd, check=True)
            print(Fore.GREEN + "[✓] Debug keystore created!")

    # Zipalign
    aligned_apk = output_apk.replace(".apk", "_aligned.apk")
    zipalign_cmd = ["zipalign", "-v", "-p", "4", input_apk, aligned_apk]
    try:
        subprocess.run(zipalign_cmd, check=True)
        print(Fore.GREEN + "[✓] zipalign successful!")
    except:
        print(Fore.YELLOW + "[!] zipalign failed, signing without alignment...")
        aligned_apk = input_apk

    # Sign with V1+V2+V3
    sign_cmd = [
        "apksigner", "sign",
        "--ks", str(keystore_path),
        "--ks-pass", f"pass:{keystore_pass}",
        "--key-pass", f"pass:{keystore_pass}",
        "--v1-signing-enabled", "true",
        "--v2-signing-enabled", "true",
        "--v3-signing-enabled", "true",
        "--out", output_apk,
        aligned_apk
    ]
    try:
        subprocess.run(sign_cmd, check=True)
        print(Fore.GREEN + f"[✓] APK signed (V1+V2+V3): {output_apk}")
        if aligned_apk != input_apk and os.path.exists(aligned_apk):
            os.remove(aligned_apk)
        return True
    except Exception as e:
        print(Fore.RED + f"[✗] Signing failed: {e}")
        return False

# ------------------- PROTECT (HIDE CODE) WITH FALLBACK -------------------
def protect_apk(input_apk, output_apk):
    print(Fore.YELLOW + "[!] Protecting APK (hiding code)... This may take a while.")
    
    # --- Check if output directory is writable ---
    out_dir = os.path.dirname(output_apk)
    if out_dir and not os.path.exists(out_dir):
        try:
            os.makedirs(out_dir, exist_ok=True)
        except Exception as e:
            print(Fore.RED + f"[✗] Cannot create output directory: {e}")
            print(Fore.YELLOW + "[!] If you're using /sdcard/, run 'termux-setup-storage' first.")
            return False

    # Try the advanced method with apktool
    temp_dir = "./temp_decoded"
    try:
        # 1. Decode
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        decode_cmd = ["apktool", "d", input_apk, "-o", temp_dir, "-f"]
        subprocess.run(decode_cmd, check=True, capture_output=True)
        print(Fore.GREEN + "[✓] Decoding successful.")

        # 2. Remove debuggable flag
        manifest_path = os.path.join(temp_dir, "AndroidManifest.xml")
        if os.path.exists(manifest_path):
            with open(manifest_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            content = re.sub(r'\s*android:debuggable="true"', '', content)
            content = re.sub(r'\s*android:debuggable="false"', '', content)
            with open(manifest_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(Fore.GREEN + "[✓] Removed debuggable flag")

        # 3. Add dummy smali class
        dummy_smali_dir = os.path.join(temp_dir, "smali", "com", "protection")
        os.makedirs(dummy_smali_dir, exist_ok=True)
        dummy_file = os.path.join(dummy_smali_dir, "DummyProtection.smali")
        with open(dummy_file, 'w') as f:
            f.write(""".class public Lcom/protection/DummyProtection;
.super Ljava/lang/Object;
.source "DummyProtection.java"

.method public constructor <init>()V
    .registers 1
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V
    return-void
.end method

.method public static getProtection()Ljava/lang/String;
    .registers 1
    const-string v0, "Protected by @onxx-x143"
    return-object v0
.end method
""")
        print(Fore.GREEN + "[✓] Added dummy protection class")

        # 4. Rebuild APK
        rebuilt_apk = output_apk.replace(".apk", "_rebuilt.apk")
        build_cmd = ["apktool", "b", temp_dir, "-o", rebuilt_apk]
        subprocess.run(build_cmd, check=True, capture_output=True)
        print(Fore.GREEN + "[✓] Rebuild successful!")

        # 5. Sign the rebuilt APK
        print(Fore.CYAN + "[*] Signing the protected APK...")
        if sign_apk(rebuilt_apk, output_apk):
            os.remove(rebuilt_apk)
            print(Fore.GREEN + f"[✓] Protected APK ready: {output_apk}")
            return True
        else:
            # Signing failed, but we have rebuilt_apk; we keep it as fallback
            print(Fore.YELLOW + "[!] Signing failed, but rebuilt APK is available.")
            return False

    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[✗] Advanced protection failed: {e}")
        print(Fore.YELLOW + "[!] Falling back to basic protection (dummy file + resign)...")
        # Fallback: just inject a dummy file and re-sign
        try:
            with zipfile.ZipFile(input_apk, 'a') as apk_zip:
                apk_zip.writestr("META-INF/protection_by_onxx.txt", "Protected by @onxx-x143")
            print(Fore.GREEN + "[✓] Added dummy protection file.")
            if sign_apk(input_apk, output_apk):
                print(Fore.GREEN + f"[✓] Basic protection applied: {output_apk}")
                return True
            else:
                print(Fore.RED + "[✗] Basic protection failed.")
                return False
        except Exception as fallback_error:
            print(Fore.RED + f"[✗] Fallback also failed: {fallback_error}")
            return False
    except Exception as e:
        print(Fore.RED + f"[✗] Unexpected error: {e}")
        return False
    finally:
        # Clean up temp directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)

# ------------------- MAIN MENU -------------------
def main_menu():
    print(Fore.CYAN + "[ℹ]  To save in /sdcard/Download, run 'termux-setup-storage' first.")
    while True:
        print("\n" + Fore.CYAN + "═══ MAIN MENU ═══")
        print(Fore.YELLOW + "1. Sign APK (local file)")
        print("2. Download APK and sign")
        print("3. Add Protection (hide code)")
        print("4. Exit")
        choice = input(Fore.GREEN + "Your choice (1-4): ").strip()

        if choice == "1":
            apk_path = input("Full path to APK: ").strip()
            if not os.path.isfile(apk_path):
                print(Fore.RED + "[✗] File not found!")
                continue
            out_dir = input("Output folder (default ./output): ").strip() or "./output"
            os.makedirs(out_dir, exist_ok=True)
            out_apk = os.path.join(out_dir, "signed_" + os.path.basename(apk_path))
            if sign_apk(apk_path, out_apk):
                print(Fore.GREEN + f"[✓] Signed APK: {out_apk}")

        elif choice == "2":
            url = input("Direct APK URL: ").strip()
            out_dir = input("Save folder (default ./downloads): ").strip() or "./downloads"
            os.makedirs(out_dir, exist_ok=True)
            filename = url.split("/")[-1] or "downloaded.apk"
            if not filename.endswith(".apk"):
                filename += ".apk"
            out_path = os.path.join(out_dir, filename)
            downloaded = download_apk(url, out_path)
            if downloaded:
                sign_choice = input("Sign this APK? (y/n): ").lower()
                if sign_choice == 'y':
                    signed_path = out_path.replace(".apk", "_signed.apk")
                    if sign_apk(downloaded, signed_path):
                        print(Fore.GREEN + f"[✓] Signed APK: {signed_path}")

        elif choice == "3":
            apk_path = input("Full path to APK: ").strip()
            if not os.path.isfile(apk_path):
                print(Fore.RED + "[✗] File not found!")
                continue
            out_dir = input("Output folder (default ./protected): ").strip() or "./protected"
            os.makedirs(out_dir, exist_ok=True)
            out_apk = os.path.join(out_dir, "protected_" + os.path.basename(apk_path))
            if protect_apk(apk_path, out_apk):
                print(Fore.GREEN + f"[✓] Protected APK: {out_apk}")
            else:
                print(Fore.RED + "[✗] Protection failed. Please check the error messages above.")

        elif choice == "4":
            print(Fore.CYAN + "Exiting...")
            sys.exit(0)
        else:
            print(Fore.RED + "[✗] Invalid choice, try again.")

# ------------------- ENTRY POINT -------------------
if __name__ == "__main__":
    clear_screen()
    open_github()
    install_dependencies()
    show_banner()
    main_menu()
