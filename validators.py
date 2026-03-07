"""
Validation logic for user input.
"""


def is_numeric_only(value: str) -> bool:
    """Return True if value is purely numeric (int or float)."""
    if not value or not value.strip():
        return False
    try:
        float(value.strip())
        return True
    except ValueError:
        return False


def looks_like_email(s: str) -> bool:
    """Basic email format check: contains @ and at least one dot after @."""
    s = (s or "").strip()
    return "@" in s and "." in s and len(s) > 3


def validate_registration(
    email: str,
    first_name: str,
    last_name: str,
    password: str,
    dob: str,
) -> tuple:
    """
    Validate registration fields in sequence (a-f).
    Returns (True, "") if valid else (False, error_message).
    """
    if not (email and email.strip()):
        return False, "Please fill all the data for registration.\nEnter Email."
    if is_numeric_only(email):
        return False, "Email should not be a number. Please enter a valid email."
    if not looks_like_email(email):
        return False, "Please enter a valid email address (e.g. name@domain.com)."

    if not (first_name and first_name.strip()):
        return False, "Please fill all the data for registration.\nEnter First Name."
    if is_numeric_only(first_name):
        return False, "First Name should not be a number. Please enter a valid first name."

    if not (last_name and last_name.strip()):
        return False, "Please fill all the data for registration.\nEnter Last Name."
    if is_numeric_only(last_name):
        return False, "Last Name should not be a number. Please enter a valid last name."

    if not (password and password.strip()):
        return False, "Please fill all the data for registration.\nEnter Password."
    if is_numeric_only(password):
        return False, "Password should not be only numbers. Please enter a valid password."

    if not (dob and dob.strip()):
        return False, "Please fill all the data for registration.\nEnter Date of Birth."
    if is_numeric_only(dob) and len(dob.strip()) <= 4:
        return False, "Date of Birth should not be only numbers (e.g. use DD/MM/YYYY). Please enter a valid date."

    return True, ""
