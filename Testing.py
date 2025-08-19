# =========================================
# Windows 11 Security Checker Tool
# A terminal-based Python tool for:
#   1. Checking Installed Software
#   2. Checking Windows Defender Status
#   3. Checking Windows Update Status
#   4. Running Malware Scan
# Designed for Windows 11
# =========================================

import subprocess

# -----------------------------
# Installed Software
# -----------------------------
def check_installed_software():
    print("\n[Checking Installed Software]")
    try:
        # گرفتن لیست نرم‌افزارهای نصب‌شده با PowerShell
        result = subprocess.check_output(
            'powershell -Command "Get-Package | Select-Object -Property Name, Version"',
            shell=True, text=True, errors="ignore"
        )
        print(result[:1000])  # برای جلوگیری از طول زیاد، فقط 1000 کاراکتر اول چاپ میشه
        print("... (List truncated)")
    except Exception as e:
        print("Error checking installed software:", e)

# -----------------------------
# Windows Defender Status
# -----------------------------
def check_windows_defender():
    print("\n[Checking Windows Defender]")
    try:
        result = subprocess.check_output(
            'powershell -Command "Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled"',
            shell=True, text=True, errors="ignore"
        )
        print(result)
    except Exception as e:
        print("Error checking Windows Defender:", e)

# -----------------------------
# Windows Update Status
# -----------------------------
def check_windows_update():
    print("\n[Checking Windows Update]")
    try:
        result = subprocess.check_output(
            'powershell -Command "Get-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot"',
            shell=True, text=True, errors="ignore"
        )
        print(result if result.strip() else "No pending updates found.")
    except Exception as e:
        print("Error checking Windows Update (you may need PSWindowsUpdate module):", e)

# -----------------------------
# Malware Check
# -----------------------------
def check_malware():
    print("\n[Checking for Malware]")
    try:
        result = subprocess.check_output(
            'powershell -Command "Start-MpScan -ScanType QuickScan"',
            shell=True, text=True, errors="ignore"
        )
        print("Quick scan started with Windows Defender.")
        print(result)
    except Exception as e:
        print("Error running malware scan:", e)

# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\nSecurity Checker Menu")
        print("----------------------")
        print("1. Installed Software")
        print("2. Windows Defender Status")
        print("3. Windows Update Status")
        print("4. Malware Check")
        print("5. Exit")
        print("----------------------")

        choice = input("Enter your choice [1-5]: ")

        if choice == "1":
            check_installed_software()
        elif choice == "2":
            check_windows_defender()
        elif choice == "3":
            check_windows_update()
        elif choice == "4":
            check_malware()
        elif choice == "5":
            print("Exiting Security Checker...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()