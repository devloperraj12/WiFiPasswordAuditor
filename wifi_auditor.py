import re
import math
from datetime import datetime
import os

COMMON_PASSWORDS = [
    "password", "password123", "12345678",
    "123456789", "admin123", "qwerty",
    "welcome", "wifi123", "internet",
    "abc123", "letmein"
]

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"\d", password):
        charset += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


def audit_wifi_password():

    print("=" * 65)
    print("             WIFI SECURITY AUDIT SUITE")
    print("=" * 65)

    ssid = input("\nEnter Wi-Fi Network Name (SSID): ")
    password = input("Enter Wi-Fi Password: ")

    reuse = input(
        "Is this password used on other websites/accounts? (yes/no): "
    ).lower()

    score = 0
    recommendations = []

    # Length
    if len(password) >= 12:
        score += 20
    else:
        recommendations.append("Use at least 12 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        recommendations.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 20
    else:
        recommendations.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 20
    else:
        recommendations.append("Add numbers")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        recommendations.append("Add special characters")

    # Common password detection
    common_password = False

    if password.lower() in COMMON_PASSWORDS:
        score -= 30
        common_password = True

    if score < 0:
        score = 0

    entropy = calculate_entropy(password)

    # Grade
    if score < 40:
        strength = "WEAK"
        grade = "D"
        risk = "HIGH"

    elif score < 70:
        strength = "MEDIUM"
        grade = "C"
        risk = "MEDIUM"

    elif score < 90:
        strength = "STRONG"
        grade = "B"
        risk = "LOW"

    elif score < 100:
        strength = "VERY STRONG"
        grade = "A"
        risk = "LOW"

    else:
        strength = "EXCELLENT"
        grade = "A+"
        risk = "VERY LOW"

    # WPA Recommendation
    if score >= 90:
        wifi_security = "WPA3 Recommended"

    elif score >= 70:
        wifi_security = "WPA2 Secure"

    else:
        wifi_security = "Upgrade Security Settings"

    # Resistance
    if entropy >= 80:
        resistance = "HIGH"

    elif entropy >= 60:
        resistance = "MEDIUM"

    else:
        resistance = "LOW"

    # Strength Meter
    filled = score // 5
    meter = "█" * filled + "░" * (20 - filled)

    print("\n")
    print("=" * 65)
    print("                WIFI SECURITY DASHBOARD")
    print("=" * 65)

    print(f"SSID                  : {ssid}")
    print(f"Password Length       : {len(password)}")
    print(f"Security Score        : {score}/100")
    print(f"Security Grade        : {grade}")
    print(f"Risk Level            : {risk}")
    print(f"Password Entropy      : {entropy:.2f} bits")
    print(f"Attack Resistance     : {resistance}")
    print(f"Wi-Fi Recommendation  : {wifi_security}")

    print("\nPASSWORD STRENGTH")
    print("-" * 65)
    print(strength)
    print(f"[{meter}] {score}%")

    print("\nSECURITY CHECKS")
    print("-" * 65)

    print("[✓] Uppercase Letters"
          if re.search(r"[A-Z]", password)
          else "[✗] Uppercase Letters")

    print("[✓] Lowercase Letters"
          if re.search(r"[a-z]", password)
          else "[✗] Lowercase Letters")

    print("[✓] Numbers"
          if re.search(r"\d", password)
          else "[✗] Numbers")

    print("[✓] Special Characters"
          if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
          else "[✗] Special Characters")

    print("[✓] Length >= 12"
          if len(password) >= 12
          else "[✗] Length < 12")

    if common_password:
        print("\n⚠ WARNING: Common password detected.")

    if reuse == "yes":
        print("⚠ WARNING: Password reuse detected.")

    print("\nSECURITY RECOMMENDATIONS")
    print("-" * 65)

    print("✓ Enable WPA3 if supported")
    print("✓ Disable WPS")
    print("✓ Change password every 6 months")
    print("✓ Use Guest Network for visitors")

    if recommendations:
        for item in recommendations:
            print(f"➜ {item}")

    else:
        print("No Security Issues Found.")

    # Report
    with open("wifi_audit_report.txt", "w") as report:

        report.write("WIFI SECURITY AUDIT REPORT\n")
        report.write("=" * 65 + "\n")
        report.write(f"Generated: {datetime.now()}\n\n")

        report.write(f"SSID: {ssid}\n")
        report.write(f"Password Length: {len(password)}\n")
        report.write(f"Security Score: {score}/100\n")
        report.write(f"Grade: {grade}\n")
        report.write(f"Risk Level: {risk}\n")
        report.write(f"Entropy: {entropy:.2f} bits\n")
        report.write(f"Attack Resistance: {resistance}\n")
        report.write(f"Wi-Fi Recommendation: {wifi_security}\n\n")

        report.write("Recommendations:\n")

        if recommendations:
            for item in recommendations:
                report.write(f"- {item}\n")
        else:
            report.write("No Security Issues Found\n")

        report.write("\nBest Practices:\n")
        report.write("- Enable WPA3\n")
        report.write("- Disable WPS\n")
        report.write("- Use Guest Network\n")
        report.write("- Avoid Password Reuse\n")

    print("\nReport saved as wifi_audit_report.txt")
    print("=" * 65)


def view_report():

    if os.path.exists("wifi_audit_report.txt"):

        print("\n")
        print("=" * 65)
        print("LAST AUDIT REPORT")
        print("=" * 65)

        with open("wifi_audit_report.txt", "r") as file:
            print(file.read())

    else:
        print("\nNo report found.")


while True:

    print("\n")
    print("=" * 65)
    print("             WIFI SECURITY AUDIT SUITE")
    print("=" * 65)

    print("1. Start Wi-Fi Security Audit")
    print("2. View Last Report")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        audit_wifi_password()

    elif choice == "2":
        view_report()

    elif choice == "3":
        print("\nExiting...")
        break

    else:
        print("\nInvalid Choice.")
