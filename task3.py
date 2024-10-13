# The task 3 of the Prodigy Infotech Internship program--Password complexity checker


def check_password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_+=<>?/.,;:" for char in password)
    strength = 0
    if length_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if upper_criteria:
        strength += 1
    if lower_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1
    if strength == 5:
        return "Very Strong"
    elif 3 <= strength < 5:
        return "Strong"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"
password = input("Enter your password: ")
print(f"Password Strength: {check_password_strength(password)}")
