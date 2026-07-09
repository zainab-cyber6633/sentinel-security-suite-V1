from modules.ping import ping_host
from modules.dns_lookup import dns_lookup
from modules.port_scanner import port_scan
from modules.whois_lookup import whois_lookup
from modules.banner_grabber import banner_grab
from modules.report import generate_report

# ==========================================
# Sentinel Security Suite
# Version : 1.0
# Author  : Zainab Ijaz
# ==========================================


def banner():
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


def menu():
    print("=" * 50)
    print("1. Ping Host")
    print("2. Port Scanner")
    print("3. DNS Lookup")
    print("4. WHOIS Lookup")
    print("5. Banner Grabber")
    print("6. Exit")
    print("=" * 50)


def main():

    banner()

    while True:

        menu()

        choice = input("Choose an option: ")

        if choice == "1":

            target = input("\nEnter target: ")

            result = ping_host(target)

            print(result)

            generate_report(
                "Ping Result",
                result
            )

        elif choice == "2":

            target = input("\nEnter target: ")

            result = port_scan(target)

            print(result)

            generate_report(
                "Port Scanner Result",
                result
            )

        elif choice == "3":

            target = input("\nEnter domain: ")

            result = dns_lookup(target)

            print(result)

            generate_report(
                "DNS Lookup Result",
                result
            )

        elif choice == "4":

            target = input("\nEnter domain: ")

            result = whois_lookup(target)

            print(result)

            generate_report(
                "WHOIS Result",
                result
            )

        elif choice == "5":

            target = input("\nEnter target: ")

            port = int(input("Enter port: "))

            result = banner_grab(target, port)

            print(result)

            generate_report(
                "Banner Grab Result",
                result
            )

        elif choice == "6":

            print("\nThank you for using Sentinel Security Suite!")
            print("Developed by Zainab Ijaz")
            print("Stay Secure 🛡️")

            break

        else:

            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()