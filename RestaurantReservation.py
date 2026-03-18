"""
Restaurant Reservation System - Entry point.

This file is the starting point of the application.
When the program is executed, Python runs this file first.
1. Import the main GUI application class
2. Create the application object
3. Start the program
"""

# Import the main application class that controls the GUI
from app import RestaurantReservationApp


# The following condition ensures that the program only runs
# when this file is executed directly.
# If the file were imported somewhere else, the program would not start automatically.
if __name__ == "__main__":

    # Create the main application object
    app = RestaurantReservationApp()

    # Start the Tkinter application loop
    # This launches the GUI and keeps the program running
    app.run()