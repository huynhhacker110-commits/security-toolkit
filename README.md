# Security Toolkit 🛡️🔴🔵

Red Team + Blue Team Penetration Testing & Vulnerability Scanning Framework

## Features

### Red Team (Offensive)
- 🔍 **Port Scanning** - TCP/UDP port enumeration
- 🎯 **Service Detection** - Identify running services and versions
- 🔐 **Vulnerability Scanning** - Detect known vulnerabilities
- 🚀 **Exploitation** - Automated exploit execution
- 📊 **Reconnaissance** - Information gathering

### Blue Team (Defensive)
- 🛡️ **Security Monitoring** - Real-time threat detection
- 📋 **Vulnerability Assessment** - Generate security reports
- 🔔 **Alert System** - Notify on suspicious activities
- 📈 **Risk Analysis** - Calculate risk scores
- 🗂️ **Remediation Suggestions** - Security recommendations

## Installation

```bash
git clone https://github.com/huynhhacker110-commits/security-toolkit.git
cd security-toolkit
pip install -r requirements.txt
```

## Usage

### Red Team
```bash
python main.py --mode red --target <target_ip> --scan-type full
```

### Blue Team
```bash
python main.py --mode blue --monitor --output report.html
```

## Project Structure

```
security-toolkit/
├── red_team/          # Offensive security modules
├── blue_team/         # Defensive security modules
├── core/              # Core utilities
├── exploits/          # Exploitation database
├── config/            # Configuration files
└── reports/           # Generated reports
```

## Requirements

- Python 3.8+
- Kali Linux / Linux-based OS
- Network access (authorized testing only)

## ⚠️ Legal Notice

**This tool is for authorized security testing ONLY!**
- Only use on systems you own or have explicit permission to test
- Unauthorized access to computer systems is illegal
- The authors assume no liability for misuse

## Contributing

Contributions are welcome! Submit pull requests for:
- New scanning modules
- Additional exploits
- Bug fixes
- Documentation improvements

## License

MIT License - See LICENSE file for details

## Author

Huynh Hacker 🔐
