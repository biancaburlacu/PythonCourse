# Write a program that checks which of the passwords inside PASSWORDS meet the 3 following criteria:
# 1. Minimum characters of 7
# 2. Must contain at least one special character (defined in SPECIAL_CHARACTERS)
# 3. Must include at least one number
# Tip: You may want to loop over PASSWORDS and use multiple if conditions
MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
PASSWORDS = ['helloWorld', 'imcisamazing69', 'ilovecookies!23', 'python1s@mazingLanguage', "#%%@#$@$#"]


def has_special_char(text):
    return any(SPECIAL_CHARS.count(char) > 0 for char in text)


def has_numbers(text):
    return any(char.isdigit() for char in text)


def has_length(text):
    return len(text) >= MIN_CHARACTERS


def is_password_valid(password):
    return has_special_char(password) and has_length(password) and has_numbers(password)


def check_password(passwords):
    for password in passwords:
        if is_password_valid(password):
            print(f"{password} is a valid password!")
        else:
            print(f"{password} is not a valid password!")
