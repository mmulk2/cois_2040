"""
Reservation file handling.
"""

from config import RESERVATIONS_FILE
from models import Reservation


class ReservationService:
    """Handles saving, loading, updating, and deleting reservations."""

    def save_reservation(self, reservation: Reservation) -> None:
        """
        Save a new reservation to the reservations file.

        This method opens the file in append mode ("a"),
        so each new reservation is added to the end of the file
        without deleting existing reservations.
        """
        with open(RESERVATIONS_FILE, "a", encoding="utf-8") as file:
            file.write(reservation.to_file_line())

    def get_reservations_by_email(self, email: str):
        """
        Return all reservations that belong to a specific user email.

        The file is read line by line.
        Each line is split using the pipe character "|".
        If the email in the file matches the requested email,
        a Reservation object is created and added to the list.
        """
        reservations = []

        try:
            with open(RESERVATIONS_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split("|")
                    if len(data) == 6 and data[0] == email:
                        reservations.append(
                            Reservation(
                                email=data[0],
                                number_of_days=data[1],
                                from_date=data[2],
                                to_date=data[3],
                                number_of_persons=data[4],
                                number_of_rooms=data[5],
                            )
                        )
        except FileNotFoundError:
            # If the file does not exist yet, return an empty list
            return []

        return reservations

    def get_reservation_by_email(self, email: str):
        """
        Return the first reservation found for the given email.

        This method uses get_reservations_by_email() and returns:
        - the first reservation if at least one exists
        - None if no reservation exists
        """
        reservations = self.get_reservations_by_email(email)
        return reservations[0] if reservations else None

    def update_reservation(self, original_reservation: Reservation, updated_reservation: Reservation) -> None:
        """
        Update one reservation in the reservations file.
        1. Read all lines from the reservation file
        2. Open the file again in write mode ("w")
        3. Rewrite every line back into the file
        4. When the matching original reservation is found,
           replace it with the updated reservation

        The variable 'updated' ensures that only the first exact match is replaced.
        """
        lines = []

        try:
            with open(RESERVATIONS_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            # If the reservation file does not exist, there is nothing to update
            return

        updated = False

        with open(RESERVATIONS_FILE, "w", encoding="utf-8") as file:
            for line in lines:
                data = line.strip().split("|")

                if (
                    not updated
                    and len(data) == 6
                    and data[0] == original_reservation.email
                    and data[1] == original_reservation.number_of_days
                    and data[2] == original_reservation.from_date
                    and data[3] == original_reservation.to_date
                    and data[4] == original_reservation.number_of_persons
                    and data[5] == original_reservation.number_of_rooms
                ):
                    file.write(updated_reservation.to_file_line())
                    updated = True
                else:
                    file.write(line)

    def delete_reservation(self, reservation_to_delete: Reservation) -> None:
        """
        Delete one reservation from the reservations file.
        1. Read all lines from the reservation file
        2. Open the file again in write mode ("w")
        3. Rewrite every line except the one that matches the reservation to delete

        The variable 'deleted' ensures that only the first exact matching reservation is removed.
        """
        lines = []

        try:
            with open(RESERVATIONS_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            # If the file does not exist, there is nothing to delete
            return

        deleted = False

        with open(RESERVATIONS_FILE, "w", encoding="utf-8") as file:
            for line in lines:
                data = line.strip().split("|")

                if (
                    not deleted
                    and len(data) == 6
                    and data[0] == reservation_to_delete.email
                    and data[1] == reservation_to_delete.number_of_days
                    and data[2] == reservation_to_delete.from_date
                    and data[3] == reservation_to_delete.to_date
                    and data[4] == reservation_to_delete.number_of_persons
                    and data[5] == reservation_to_delete.number_of_rooms
                ):
                    deleted = True
                    continue

                file.write(line)