"""
Data models used by the Restaurant Reservation System.

This file contains the classes that represent the main objects
used in the system:

1. RegisterUser represents a registered user
2. Reservation represents a reservation made by a user

These classes are responsible for holding data and converting
that data into a format that can be saved to text files.
"""


class RegisterUser:
    """
    Represents a registered user in the system.

    Each user has:
    - email
    - first name
    - last name
    - password
    - date of birth
    """

    def __init__(self, email: str, firstName: str, lastName: str, password: str, dob: str):
        """
        Constructor for creating a new RegisterUser object.

        Parameters:
        email= user's email (used for login)
        firstName= user's first name
        lastName= user's last name
        password= user's password
        dob= user's date of birth
        """
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.dob = dob

    def to_file_line(self) -> str:
        """
        Convert the user object into a string that can be written to the file.

        The data is separated using the "|" character so that it can be
        easily split when reading the file later.

        Example stored line:
        email|firstName|lastName|password|dob
        """
        return f"{self.email}|{self.firstName}|{self.lastName}|{self.password}|{self.dob}\n"


class Reservation:
    """
    Represents a reservation made by a user.

    Each reservation stores:
    - email of the user who made the reservation
    - number of days
    - from date
    - to date
    - number of persons
    - number of rooms
    """

    def __init__(
        self,
        email: str,
        number_of_days: str,
        from_date: str,
        to_date: str,
        number_of_persons: str,
        number_of_rooms: str,
    ):
        """
        Constructor for creating a Reservation object.

        Parameters:
        email = email of the user who made the reservation
        number_of_days=length of the reservation
        from_date =starting date of reservation
        to_date= ending date of reservation
        number_of_persons= how many people are included
        number_of_rooms= number of rooms reserved
        """
        self.email = email
        self.number_of_days = number_of_days
        self.from_date = from_date
        self.to_date = to_date
        self.number_of_persons = number_of_persons
        self.number_of_rooms = number_of_rooms

    def to_file_line(self) -> str:
        """
        Convert the reservation object into a string for saving in the file.

        Format used in the reservation file:
        email|days|from_date|to_date|persons|rooms
        """
        return (
            f"{self.email}|{self.number_of_days}|{self.from_date}|"
            f"{self.to_date}|{self.number_of_persons}|{self.number_of_rooms}\n"
        )