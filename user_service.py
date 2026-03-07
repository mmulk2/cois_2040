"""
Service layer for user persistence and authentication.
"""

from typing import List, Tuple

from config import USERS_FILE
from models import RegisterUser


class UserService:
    """Handles loading, saving, and verifying users."""

    def __init__(self, users_file: str = USERS_FILE):
        self._users_file = users_file

    def save_user(self, user: RegisterUser) -> None:
        """Append a registered user to the file."""
        with open(self._users_file, "a", encoding="utf-8") as f:
            f.write(user.to_file_line())

    def load_users(self) -> List[Tuple[str, str]]:
        """Load registered users from file. Returns list of (email, password) tuples."""
        users = []
        try:
            with open(self._users_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("|")
                    if len(parts) >= 4:
                        email, first_name, last_name, password = (
                            parts[0],
                            parts[1],
                            parts[2],
                            parts[3],
                        )
                        users.append((email.strip(), password.strip()))
        except FileNotFoundError:
            pass
        return users

    def verify_login(self, email: str, password: str) -> bool:
        """Return True if email and password match a registered user."""
        email = (email or "").strip()
        password = (password or "").strip()
        users = self.load_users()
        for stored_email, stored_password in users:
            if stored_email == email and stored_password == password:
                return True
        return False
