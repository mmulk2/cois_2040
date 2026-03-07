COIS 2040 – Restaurant Reservation System

A desktop application for restaurant reservations built with Python and Tkinter. Users can register, log in, and (in the UI) access reservation options.

---

Manzur - What’s Included

### Main menu
- **Welcome** message at the top
- **Register / Sign up** – open registration form
- **Login** – open login form (email and password)
- **Exit** – quit the application

Registration
- **Registration In-Process** form with:
  - Email
  - First Name
  - Last Name
  - Password (masked for securty purpose)
  - **Date of Birth** – three dropdowns (Month, Day, Year)
- **Validation** (in order): all fields required; email must look like an email; Email, First Name, Last Name, and Password must not be only numbers; DOB must be a valid date from the dropdowns
- **Submit** – saves user to `users_data.txt`, shows **Registration Successful**”, then returns to main menu
- **Exit** – returns to main menu without saving

Login
- **Enter your Email** and **Enter your Password**
- Press **Enter** in the password field or click **Login** to sign in
- Credentials are checked against `users_data.txt`
- **Success** – user menu with: View Reservation, Make Reservation, Modify Reservation, Cancel Reservation, Logout
- **Failure** – “The password or username you've entered is incorrect” and options: **Try again (Login)**, **Register**, **Exit (Main Menu)**

User menu (after login)
- View Reservation 
- Make Reservation 
- Modify Reservation 
- Cancel Reservation 
- **Logout** – return to main menu

### Details
- **OOP layout**: config, models, validators, user service, and app are in separate modules
- **Data storage**: users stored in `users_data.txt` (separated by: email|firstName|lastName|password|dob)
- **DOB format**: e.g. `Jan 01, 2002` (from Month/Day/Year dropdowns)
- **.gitignore**: `__pycache__/`, `users_data.txt`, venv, IDE/OS files

---

How to Run

From the project folder:

```bash
python3 RestaurantReservation.py
```


**First run:** The app will create `users_data.txt` when the first user registers. You can register from the main menu, then log in with that email and password.

---

## Project Structure

| File | Purpose |
|------|--------|
| **RestaurantReservation.py** | Entry point – run this to start the app |
| **app.py** | Main GUI: `RestaurantReservationApp` (screens, navigation) |
| **models.py** | Domain model: `RegisterUser` |
| **config.py** | Constants (e.g. `USERS_FILE`) |
| **validators.py** | Input validation (registration, email, DOB format) |
| **user_service.py** | User persistence and login: `UserService` (save, load, verify) |
| **users_data.txt** | User data file (created on first registration; ignored by Git) |
| **.gitignore** | Ignores `__pycache__/`, `users_data.txt`, venv, etc. |

---

COIS 2040 – Trent University
