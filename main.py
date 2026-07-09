from modules.ping import ping_host
# ==========================================
# Sentinel Security Suite
# Version : 1.0
# Author  : Zainab Ijaz
# ==========================================


print(r"""
   _____            _   _             _
  / ____|          | | (_)           | |
 | (___   ___ _ __ | |_ _ _ __   ___| |
  \___ \ / _ \ '_ \| __| | '_ \ / _ \ |
  ____) |  __/ | | | |_| | | | |  __/ |
 |_____/ \___|_| |_|\__|_|_| |_|\___|_|

        Sentinel Security Suite
              Version 1.0

         Developed by Zainab Ijaz

    Reconnaissance • Analysis • Security
""")

print("=" * 50)
print("1. Ping Host")
print("2. Port Scanner")
print("3. DNS Lookup")
print("4. WHOIS Lookup")
print("5. Banner Grabber")
print("6. Exit")
print("=" * 50)

choice = input("Choose an option: ")

if choice == "1":
    print("\n[+] Ping module coming soon...")

elif choice == "2":
    print("\n[+] Port Scanner coming soon...")

elif choice == "3":
    print("\n[+] DNS Lookup coming soon...")

elif choice == "4":
    print("\n[+] WHOIS Lookup coming soon...")

elif choice == "5":
    print("\n[+] Banner Grabber coming soon...")

elif choice == "6":
    print("\nThank you for using Sentinel Security Suite!")

else:
    print("\nInvalid option. Please select a valid menu option.")

target = input("Enter target: ")

result = ping_host(target)

print(result)