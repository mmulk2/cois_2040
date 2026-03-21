"""
Validation logic for user input (OOP).

All input validation for the app lives here; the GUI only displays messages
and calls services after validation succeeds.
"""

from datetime import date, datetime


class UserRegistrationValidator:
    """
    Validates user registration fields and related input rules.

    Helper methods support reuse and testing; validate_registration
    runs the full registration checklist in order.
    """

    def is_numeric_only(self, value: str) -> bool:
        """
        Return True if the given value is only numeric.

        This method tries to convert the input to a number.
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

    def looks_like_email(self, s: str) -> bool:
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

    def is_valid_dob_string(self, dob: str) -> bool:
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
        self,
        email: str,
        first_name: str,
        last_name: str,
        password: str,
        dob: str,
    ) -> tuple:
        """
        Validate all registration fields in order.

        Returns:
        - (True, "") if all fields are valid
        - (False, error_message) if any field is invalid

        Validation is done step-by-step so the user gets one clear message
        telling them what must be fixed first.
        """

        # Check that email is not empty
        if not (email and email.strip()):
            return False, "Please fill all the data for registration.\nEnter Email."

        # Check that email is not only numeric
        if self.is_numeric_only(email):
            return False, "Email should not be a number. Please enter a valid email."

        # Check that email has a simple valid format
        if not self.looks_like_email(email):
            return False, "Please enter a valid email address (e.g. name@domain.com)."

        # Check that first name is not empty
        if not (first_name and first_name.strip()):
            return False, "Please fill all the data for registration.\nEnter First Name."

        # Check that first name is not only numeric
        if self.is_numeric_only(first_name):
            return False, "First Name should not be a number. Please enter a valid first name."

        # Check that last name is not empty
        if not (last_name and last_name.strip()):
            return False, "Please fill all the data for registration.\nEnter Last Name."

        # Check that last name is not only numeric
        if self.is_numeric_only(last_name):
            return False, "Last Name should not be a number. Please enter a valid last name."

        # Check that password is not empty
        if not (password and password.strip()):
            return False, "Please fill all the data for registration.\nEnter Password."

        # Check that password is not only numeric
        if self.is_numeric_only(password):
            return False, "Password should not be only numbers. Please enter a valid password."

        # Check that date of birth is not empty
        if not (dob and dob.strip()):
            return False, "Please fill all the data for registration.\nSelect Date of Birth."

        # Check that date of birth is not only numeric
        if self.is_numeric_only(dob):
            return False, "Date of Birth must be selected from the dropdowns."

        # Check that the date of birth format is valid
        if not self.is_valid_dob_string(dob):
            return False, "Please select a valid Date of Birth (Month, Day, Year)."

        # If all checks pass, registration is valid
        return True, ""


class LoginValidator:
    """Validates login form fields before credentials are checked."""

    def validate_login(self, email: str, password: str) -> tuple:
        """
        Returns (True, "") if both fields are present, else (False, message).
        """
        email = (email or "").strip()
        password = (password or "").strip()

        if not email:
            return False, "Please enter your email."

        if not password:
            return False, "Please enter your password."

        return True, ""


class ReservationValidator:
    """Validates reservation form fields and date rules (same for create and modify)."""

    def validate_reservation(
        self,
        days: str,
        persons: str,
        rooms: str,
        from_month: str,
        from_day: str,
        from_year: str,
        to_month: str,
        to_day: str,
        to_year: str,
        today: date,
        max_date: date,
    ) -> tuple:
        """
        Validate reservation inputs built from dropdowns and text fields.

        Returns:
        - On success: (True, "", from_date_iso, to_date_iso)  e.g. "2025-03-18"
        - On failure: (False, error_message, None, None)
        """
        days = (days or "").strip()
        persons = (persons or "").strip()
        rooms = (rooms or "").strip()

        if not all([days, persons, rooms]):
            return False, "Please fill all reservation fields.", None, None

        if not days.isdigit():
            return False, "Number of Days must be a whole number.", None, None

        if not persons.isdigit():
            return False, "Number of Persons must be a whole number.", None, None

        if not rooms.isdigit():
            return False, "Number of Rooms must be a whole number.", None, None

        try:
            from_iso = (
                f"{from_year}-{datetime.strptime(from_month, '%b').month:02d}-"
                f"{int(from_day):02d}"
            )
            to_iso = (
                f"{to_year}-{datetime.strptime(to_month, '%b').month:02d}-"
                f"{int(to_day):02d}"
            )
            from_date_obj = datetime.strptime(from_iso, "%Y-%m-%d").date()
            to_date_obj = datetime.strptime(to_iso, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return False, "Please select valid dates.", None, None

        if from_date_obj < today or to_date_obj < today:
            return False, "Reservation dates cannot be in the past.", None, None

        if from_date_obj > max_date or to_date_obj > max_date:
            return (
                False,
                "Reservation dates must be within 1 year from today.",
                None,
                None,
            )

        if to_date_obj <= from_date_obj:
            return False, "To Date must be after From Date.", None, None

        return True, "", from_iso, to_iso
