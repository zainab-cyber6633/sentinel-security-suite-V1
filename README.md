<p align="center">
  <img src="assest/logo.png" alt="Sentinel Security Suite Logo" width="220">
</p>

<h1 align="center">🛡️ Sentinel Security Suite</h1>

<p align="center">
  A lightweight command-line cybersecurity toolkit built with Python for network reconnaissance and information gathering.
</p>

<p align="center">
  <strong>Version 1.0</strong> • 🚧 <strong>Version 2.0 – In Development</strong>
</p>

---

_________



#🛡️ Sentinel Security Suite

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

# Installation for linux 

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
python sentinel.py
```
## Installation for windows

git clone https://github.com/zainab-cyber6633/sentinel-security-suite.git

cd sentinel-security-suite

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python sentinel.py
     or 
 py sentinel.py    
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
__________
  # version 2 .........coming soon

_________
# License

This project is licensed under the MIT License.
