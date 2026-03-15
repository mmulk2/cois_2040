"""
Domain models for the Restaurant Reservation System.
"""

from dataclasses import dataclass


@dataclass
class RegisterUser:
    """Represents a registered user."""

    email: str
    firstName: str
    lastName: str
    password: str
    dob: str

    def __str__(self) -> str:
        return f"{self.firstName} | {self.lastName} | {self.email}"

    def to_file_line(self) -> str:
        """Format for saving to file (pipe-separated)."""
        return f"{self.email}|{self.firstName}|{self.lastName}|{self.password}|{self.dob}\n"
    
@dataclass
class Reservation:
    """Represents one reservation."""

    email: str
    number_of_days: str
    from_date: str
    to_date: str
    number_of_persons: str
    number_of_rooms: str

    def to_file_line(self) -> str:
        return (
            f"{self.email}|{self.number_of_days}|{self.from_date}|"
            f"{self.to_date}|{self.number_of_persons}|{self.number_of_rooms}\n"
        )