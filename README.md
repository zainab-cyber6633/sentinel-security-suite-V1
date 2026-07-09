
# 🛡️ Sentinel Security Suite

A lightweight command-line cybersecurity toolkit built with Python for basic network reconnaissance and information gathering.

This project was developed as a learning project to practice Python programming, networking concepts, and cybersecurity fundamentals.

---

# Features

- ✅ Ping Host
- 🌐 DNS Lookup
- 📄 WHOIS Lookup
- 🔍 TCP Port Scanner
- 🖥️ Banner Grabber
- 📝 Automatic Report Generation
- 💻 Interactive Command Line Interface

---

# Technologies Used

- Python 3
- Socket Programming
- Python WHOIS
- Subprocess Module

---

# Project Structure

```text
Sentinel-Security-Suite/
│
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
├── .gitignore
│
├── modules/
│   ├── __init__.py
│   ├── ping.py
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   ├── port_scanner.py
│   ├── banner_grabber.py
│   └── report.py
│
├── reports/
│   └── scan_report.txt
│
├── assets/
│
└── docs/
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/zainab-cyber6633/Sentinel-Security-Suite.git
```

Enter the project directory

```bash
cd Sentinel-Security-Suite
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# Usage

Launch the application.

Choose one of the available options:

- Ping Host
- Port Scanner
- DNS Lookup
- WHOIS Lookup
- Banner Grabber

After each scan, the results are displayed in the terminal and can be saved to the report file.

---

# Sample Features

### Ping Host

- Check whether a host is reachable.
- Display ping response.

### DNS Lookup

- Resolve a domain name to its IP address.

### WHOIS Lookup

- Retrieve domain registration information.

### Port Scanner

- Scan common TCP ports.
- Display open and closed ports.

### Banner Grabber

- Attempt to retrieve the service banner from a target host.

### Report Generator

- Save scan results into the `reports/scan_report.txt` file.

---

# Future Improvements

- HTTP Header Analyzer
- SSL Certificate Checker
- Reverse DNS Lookup
- Subdomain Enumeration
- Multi-threaded Port Scanner
- HTML Reports
- PDF Reports
- Colored Terminal Output

🚀 Version 2.0 — Coming Soon
---

# Author

**Zainab Ijaz**

Cybersecurity Enthusiast

Interested in:

- Penetration Testing
- Red Teaming
- Network Security
- Python Automation

---
---

# Screenshots

## Main Menu

![Main Menu](assets/menu.png)

---

## Ping Host

![Ping](assets/ping.png)

---

## DNS Lookup

![DNS Lookup](assets/dns.png)

---

## WHOIS Lookup

![WHOIS Lookup](assets/whois.png)

---

## Port Scanner

![Port Scanner](assets/portscanner.png)

---

## Banner Grabber

![Banner Grabber](assets/banner.png)


# License

This project is licensed under the MIT License.
