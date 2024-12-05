import re


def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z .]+$", name))  # Allows letters, spaces, and dots

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10  # Checks for a 10-digit number

def is_valid_country_code(code):
    return code.startswith('+') and code[1:].isdigit()  # Validates a country code like +880

def is_valid_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))  # Simple email validation

def is_valid_full_phone(phone):
    return bool(re.match(r"^\+\d{1,4}\d{10}$", phone))  # Full phone with country code (e.g., +8801712345678)
