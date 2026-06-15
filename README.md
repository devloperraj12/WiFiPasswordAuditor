# 📶 Wi-Fi Password Security Auditor

A Python-based cybersecurity tool designed to evaluate the security strength of Wi-Fi passwords and provide actionable recommendations to improve wireless network security.

---

## 📌 Project Overview

Weak Wi-Fi passwords are one of the most common causes of unauthorized network access. This project performs a comprehensive security audit of Wi-Fi passwords by analyzing password complexity, entropy, password reuse, and common password patterns.

The tool generates a detailed security assessment report and provides best-practice recommendations to help users strengthen their wireless network security.

---

## ✨ Features

* Wi-Fi Password Strength Analysis
* Security Score Calculation (0–100)
* Security Grade System (A+ to D)
* Password Entropy Calculation
* Risk Level Assessment
* Common Password Detection
* Password Reuse Warning
* WPA2/WPA3 Security Recommendation
* Attack Resistance Analysis
* Security Dashboard
* Report Generation
* Menu-Driven Interface

---

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (re)
* Math Module
* Datetime Module
* File Handling
* Kali Linux

---

## 📂 Project Structure

```text
WiFiPasswordAuditor/
│
├── wifi_auditor.py
├── wifi_audit_report.txt
├── README.md
└── screenshots/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/devloperraj12/WiFiPasswordAuditor.git
cd WiFiPasswordAuditor
```

---

## ▶️ Usage

Run the program:

```bash
python3 wifi_auditor.py
```

Menu:

```text
1. Start Wi-Fi Security Audit
2. View Last Report
3. Exit
```

---

## 📊 Sample Output

```text
=================================================================
                WIFI SECURITY DASHBOARD
=================================================================

SSID                  : CyberLab
Password Length       : 23
Security Score        : 100/100
Security Grade        : A+
Risk Level            : VERY LOW

Password Entropy      : 150.82 bits
Attack Resistance     : HIGH

Wi-Fi Recommendation  : WPA3 Recommended

PASSWORD STRENGTH

EXCELLENT

[████████████████████] 100%
```

---

## 🔒 Security Checks Performed

The auditor evaluates:

* Password Length
* Uppercase Letters
* Lowercase Letters
* Numeric Characters
* Special Characters
* Common Password Usage
* Password Reuse
* Entropy Analysis
* Wireless Security Recommendations

---

## 📄 Generated Report

The application automatically generates:

```text
wifi_audit_report.txt
```

The report contains:

* Security Score
* Security Grade
* Entropy Value
* Risk Assessment
* Attack Resistance Level
* Security Recommendations

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Wi-Fi Security Fundamentals
* Password Security Analysis
* Entropy Calculation
* Cybersecurity Risk Assessment
* Python Programming
* Report Generation
* Security Best Practices

---

## 👨‍💻 Author

**Raj Kumar Sah**

Cyber Security & Ethical Hacking Intern

GitHub: https://github.com/devloperraj12

LinkedIn: https://www.linkedin.com/in/rajkrsah17

---

## 📈 Future Enhancements

* GUI Version using Tkinter
* PDF Report Generation
* Password Breach Database Integration
* Wireless Security Compliance Checks
* Multi-Network Security Assessment
