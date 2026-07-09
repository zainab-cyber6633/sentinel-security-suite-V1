from datetime import datetime


def generate_report(title, content):

    filename = "reports/scan_report.txt"

    with open(filename, "a") as file:

        file.write("\n")
        file.write("=" * 50)
        file.write("\nSentinel Security Suite Report\n")
        file.write("=" * 50)
        file.write("\n")

        file.write(f"Generated Time: {datetime.now()}\n")

        file.write(f"\n{title}\n")
        file.write("-" * 30)
        file.write("\n")

        file.write(content)

        file.write("\n")


    print(f"\n[+] Report saved: {filename}")