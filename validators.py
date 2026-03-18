"""
Validation logic for user input.
"""

from datetime import datetime


def is_numeric_only(value: str) -> bool:
    """
    Return True if the given value is only numeric.

    This function tries to convert the input to a number.
    If it works, the value is numeric only.
    If it fails, the value contains letters or other characters.
    """
    if not value or not value.strip():
        return False
    try:
        float(value.strip())
        return True
    except ValueError:
        return False


def looks_like_email(s: str) -> bool:
    """
    Basic email format check.

    This is a simple validation rule used by the project.
    It checks that:
    - the string contains "@"
    - the string contains "."
    - the string is longer than 3 characters
    """
    s = (s or "").strip()
    return "@" in s and "." in s and len(s) > 3


def is_valid_dob_string(dob: str) -> bool:
    """
    Return True if the date of birth matches the expected format.

    Expected format:
    Mon DD, YYYY
    Example:
    Jan 29, 2007

    datetime.strptime() is used to confirm that the date is real
    and that the format is correct.
    """
    if not dob or not dob.strip():
        return False
    try:
        datetime.strptime(dob.strip(), "%b %d, %Y")
        return True
    except ValueError:
        return False


def validate_registration(
    email: str,
    first_name: str,
    last_name: str,
    password: str,
    dob: str,
) -> tuple:
    """
    Validate all registration fields in order.

    This function returns:
    - (True, "") if all fields are valid
    - (False, error_message) if any field is invalid

    Validation is done step-by-step so the user gets one clear message
    telling them what must be fixed first.
    """

    # Check that email is not empty
    if not (email and email.strip()):
        return False, "Please fill all the data for registration.\nEnter Email."

    # Check that email is not only numeric
    if is_numeric_only(email):
        return False, "Email should not be a number. Please enter a valid email."

    # Check that email has a simple valid format
    if not looks_like_email(email):
        return False, "Please enter a valid email address (e.g. name@domain.com)."

    # Check that first name is not empty
    if not (first_name and first_name.strip()):
        return False, "Please fill all the data for registration.\nEnter First Name."

    # Check that first name is not only numeric
    if is_numeric_only(first_name):
        return False, "First Name should not be a number. Please enter a valid first name."

    # Check that last name is not empty
    if not (last_name and last_name.strip()):
        return False, "Please fill all the data for registration.\nEnter Last Name."

    # Check that last name is not only numeric
    if is_numeric_only(last_name):
        return False, "Last Name should not be a number. Please enter a valid last name."

    # Check that password is not empty
    if not (password and password.strip()):
        return False, "Please fill all the data for registration.\nEnter Password."

    # Check that password is not only numeric
    if is_numeric_only(password):
        return False, "Password should not be only numbers. Please enter a valid password."

    # Check that date of birth is not empty
    if not (dob and dob.strip()):
        return False, "Please fill all the data for registration.\nSelect Date of Birth."

    # Check that date of birth is not only numeric
    if is_numeric_only(dob):
        return False, "Date of Birth must be selected from the dropdowns."

    # Check that the date of birth format is valid
    if not is_valid_dob_string(dob):
        return False, "Please select a valid Date of Birth (Month, Day, Year)."

    # If all checks pass, registration is valid
    return True, ""