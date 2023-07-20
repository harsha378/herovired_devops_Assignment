import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets the strength criteria."

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)
