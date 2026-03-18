"""
Application configuration constants.

This file stores configuration values used across the system.
Keeping them in one place makes it easier to manage file paths
and settings without editing multiple files.
"""


# File used to store registered user information.
# Each line in this file represents one user.
# Format used in the file:
# email|firstName|lastName|password|dob
USERS_FILE = "users_data.txt"


# File used to store reservations made by users.
# Each line represents one reservation.
# Format used in the file:
# email|number_of_days|from_date|to_date|number_of_persons|number_of_rooms
RESERVATIONS_FILE = "reservations_data.txt"