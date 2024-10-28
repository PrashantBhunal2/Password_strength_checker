import re

def load_common_passwords(filename):
    with open(filename, 'r') as file:
        common_passwords = set(line.strip() for line in file)
    return common_passwords


def check_password_strength(password, common_passwords):
    strength = 0
    length = len(password)

    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1
    if length >= 14:
        strength+= 1

    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r"[~!@#$%^&*()_\-+={[}\]|\:;\"'<,>.?]", password):  # Add more special characters if needed

        strength += 1

    if password in common_passwords:
        return "Weak - This password is too common"

    if strength <= 3:
        return "Weak"
    elif strength == 4:
        return "Moderate"
    elif strength ==5:
        return "Strong"
    elif strength ==6:
        return "Strong"
    elif strength >=7:
        return "Very Strong"    
    print("strength is ",strength)

common_passwords = load_common_passwords("10-million-password-list-top-100.txt")


password = input("Enter a password: ")
strength = check_password_strength(password, common_passwords)
print("Password Strength:" ,strength)
