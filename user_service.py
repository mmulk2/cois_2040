"""
User file handling.

This file manages:
- saving registered users
- verifying login credentials

All user data is stored in a text file defined in config.py.
"""

from config import USERS_FILE
from models import RegisterUser


class UserService:
    """Handles saving users and verifying login credentials."""

    def save_user(self, user: RegisterUser) -> None:
        """
        Save a new user to the users file.

        The file is opened in append mode ("a") so that
        each new user is added to the end of the file
        without removing existing users.
        """
        with open(USERS_FILE, "a", encoding="utf-8") as file:
            # Convert the RegisterUser object to a file string
            file.write(user.to_file_line())

    def verify_login(self, email: str, password: str) -> bool:
        """
        Verify that the provided email and password match a saved user.
        1. Open the user data file
        2. Read each line
        3. Split the line into fields using "|"
        4. Compare the email and password fields
        If a matching user is found, return True.
        If no match is found, return False.
        """

        try:
            with open(USERS_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    # Split stored user data into parts
                    data = line.strip().split("|")

                    # Check that the file line has the correct number of fields
                    if len(data) >= 4:
                        stored_email = data[0]
                        stored_password = data[3]

                        # Compare entered login credentials with stored credentials
                        if stored_email == email and stored_password == password:
                            return True

        except FileNotFoundError:
            """
            If the users file does not exist yet,
            it means no users have registered.
            """
            return False

        # If no matching credentials were found
        return False