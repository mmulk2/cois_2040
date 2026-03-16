"""
Main application controller - Tkinter GUI for Restaurant Reservation System.
Uses models, validators, and UserService following OOP separation of concerns.
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from models import RegisterUser, Reservation
from user_service import UserService
from reservation_service import ReservationService
from validators import validate_registration


class RestaurantReservationApp:
    """Main application: manages window and navigation between screens."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurant Reservation System")
        self.root.geometry("520x480")
        self.root.minsize(480, 420)
        self.root.resizable(True, True)
        self.root.configure(bg="#f5f5f5")

        self._user_service = UserService()
        self._reservation_service = ReservationService()
        self.logged_in_email = None

        self.show_main_menu()

    def clear_window(self) -> None:
        for w in self.root.winfo_children():
            w.destroy()

    def show_main_menu(self) -> None:
        self.clear_window()

        welcome = tk.Label(
            self.root,
            text="Welcome to Our Restaurant Reservation System",
            font=("Helvetica", 16, "bold"),
            fg="#1a1a1a",
            bg="#f5f5f5",
        )
        welcome.pack(pady=(24, 8))

        sub = tk.Label(
            self.root,
            text="Please select an option below",
            font=("Helvetica", 12),
            fg="#333333",
            bg="#f5f5f5",
        )
        sub.pack(pady=(0, 24))

        btn_frame = tk.Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(pady=10)

        btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 22,
            "height": 2,
            "relief": tk.RAISED,
            "cursor": "hand2",
            "borderwidth": 2,
            "highlightbackground": "#2c3e50",
            "highlightthickness": 1,
            "fg": "#1a1a1a",
            "activeforeground": "#1a1a1a",
        }

        tk.Button(
            btn_frame,
            text="Register / Sign up",
            bg="#3498db",
            activebackground="#2980b9",
            command=self.show_registration,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Login",
            bg="#2ecc71",
            activebackground="#27ae60",
            command=self.show_login,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Exit",
            bg="#e74c3c",
            activebackground="#c0392b",
            command=self._exit_app,
            **btn_style,
        ).pack(pady=6)

    def show_login(self) -> None:
        self.clear_window()

        title = tk.Label(
            self.root,
            text="Login",
            font=("Helvetica", 16, "bold"),
            fg="#1a1a1a",
            bg="#f5f5f5",
        )
        title.pack(pady=(24, 16))

        content = tk.Frame(self.root, bg="#f5f5f5")
        content.pack(fill=tk.BOTH, expand=True)

        tk.Frame(content, bg="#f5f5f5", height=1).pack(fill=tk.Y, expand=True)

        form = tk.Frame(content, padx=20, pady=10, bg="#f5f5f5")
        form.pack(fill=tk.X)

        tk.Label(
            form,
            text="Enter your Email:",
            font=("Helvetica", 12, "bold"),
            anchor="w",
            fg="#1a1a1a",
            bg="#f5f5f5",
        ).grid(row=0, column=0, sticky="w", pady=4)

        email_outer = tk.Frame(
            form, highlightbackground="#888888", highlightthickness=2, bg="#888888"
        )
        email_outer.grid(row=0, column=1, pady=4, padx=(8, 0), sticky="ew")

        email_var = tk.StringVar()
        tk.Entry(
            email_outer,
            textvariable=email_var,
            width=33,
            font=("Helvetica", 12),
            fg="#1a1a1a",
            bg="#ffffff",
            insertbackground="#1a1a1a",
            relief=tk.FLAT,
        ).pack(padx=2, pady=2, fill=tk.BOTH, expand=True)

        tk.Label(
            form,
            text="Enter your Password:",
            font=("Helvetica", 12, "bold"),
            anchor="w",
            fg="#1a1a1a",
            bg="#f5f5f5",
        ).grid(row=1, column=0, sticky="w", pady=4)

        pw_outer = tk.Frame(
            form, highlightbackground="#888888", highlightthickness=2, bg="#888888"
        )
        pw_outer.grid(row=1, column=1, pady=4, padx=(8, 0), sticky="ew")

        password_var = tk.StringVar()
        password_entry = tk.Entry(
            pw_outer,
            textvariable=password_var,
            width=33,
            font=("Helvetica", 12),
            fg="#1a1a1a",
            bg="#ffffff",
            insertbackground="#1a1a1a",
            relief=tk.FLAT,
            show="*",
        )
        password_entry.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)

        def do_login() -> None:
            email = email_var.get().strip()
            password = password_var.get().strip()

            if not email:
                messagebox.showwarning("Login", "Please enter your email.")
                return

            if not password:
                messagebox.showwarning("Login", "Please enter your password.")
                return

            if self._user_service.verify_login(email, password):
                self.logged_in_email = email
                self.show_user_menu()
            else:
                self.show_failed_login_options()

        password_entry.bind("<Return>", lambda e: do_login())

        btn_frame = tk.Frame(content, bg="#f5f5f5")
        btn_frame.pack(pady=16)

        login_btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 14,
            "height": 2,
            "relief": tk.RAISED,
            "cursor": "hand2",
            "borderwidth": 2,
            "highlightbackground": "#2c3e50",
            "fg": "#1a1a1a",
            "activeforeground": "#1a1a1a",
        }

        tk.Button(
            btn_frame,
            text="Login",
            bg="#2ecc71",
            activebackground="#27ae60",
            command=do_login,
            **login_btn_style,
        ).pack(pady=8)

        tk.Frame(content, bg="#f5f5f5", height=1).pack(fill=tk.Y, expand=True)

    def show_failed_login_options(self) -> None:
        self.clear_window()

        tk.Label(
            self.root,
            text="Login Failed",
            font=("Helvetica", 16, "bold"),
            fg="#c0392b",
            bg="#f5f5f5",
        ).pack(pady=(24, 12))

        tk.Label(
            self.root,
            text="The password or username you've entered is incorrect.",
            font=("Helvetica", 12),
            fg="#1a1a1a",
            bg="#f5f5f5",
            wraplength=400,
        ).pack(pady=(0, 8))

        tk.Label(
            self.root,
            text="What would you like to do?",
            font=("Helvetica", 11),
            fg="#333333",
            bg="#f5f5f5",
        ).pack(pady=(0, 24))

        btn_frame = tk.Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(pady=10)

        btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 18,
            "height": 2,
            "relief": tk.RAISED,
            "cursor": "hand2",
            "borderwidth": 2,
            "highlightbackground": "#2c3e50",
            "fg": "#1a1a1a",
            "activeforeground": "#1a1a1a",
        }

        tk.Button(
            btn_frame,
            text="Try again (Login)",
            bg="#3498db",
            activebackground="#2980b9",
            command=self.show_login,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Register",
            bg="#2ecc71",
            activebackground="#27ae60",
            command=self.show_registration,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Exit (Main Menu)",
            bg="#95a5a6",
            activebackground="#7f8c8d",
            command=self.show_main_menu,
            **btn_style,
        ).pack(pady=6)

    def show_user_menu(self) -> None:
        self.clear_window()

        tk.Label(
            self.root,
            text="Welcome back!",
            font=("Helvetica", 16, "bold"),
            fg="#1a1a1a",
            bg="#f5f5f5",
        ).pack(pady=(24, 8))

        tk.Label(
            self.root,
            text="Please select an option",
            font=("Helvetica", 12),
            fg="#333333",
            bg="#f5f5f5",
        ).pack(pady=(0, 24))

        btn_frame = tk.Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(pady=10)

        btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 22,
            "height": 2,
            "relief": tk.RAISED,
            "cursor": "hand2",
            "borderwidth": 2,
            "highlightbackground": "#2c3e50",
            "highlightthickness": 1,
            "fg": "#1a1a1a",
            "activeforeground": "#1a1a1a",
        }

        tk.Button(
            btn_frame,
            text="View Reservation",
            bg="#3498db",
            activebackground="#2980b9",
            command=self.show_view_reservation,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Make Reservation",
            bg="#2ecc71",
            activebackground="#27ae60",
            command=self.show_make_reservation,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Modify Reservation",
            bg="#9b59b6",
            activebackground="#8e44ad",
            command=self.show_modify_reservation,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Cancel Reservation",
            bg="#e67e22",
            activebackground="#d35400",
            command=self.show_cancel_reservation,
            **btn_style,
        ).pack(pady=6)

        tk.Button(
            btn_frame,
            text="Logout",
            bg="#e74c3c",
            activebackground="#c0392b",
            command=self._do_logout,
            **btn_style,
        ).pack(pady=6)

    def _do_logout(self) -> None:
        self.logged_in_email = None
        self.show_main_menu()

    def _exit_app(self) -> None:
         messagebox.showinfo("Exit", "Thank you for using our Reservation System")
         self.root.quit()

    def show_registration(self) -> None:
        self.clear_window()

        tk.Label(
            self.root,
            text="Registration In-Process",
            font=("Helvetica", 16, "bold"),
            fg="#1a1a1a",
            bg="#f5f5f5",
        ).pack(pady=(16, 12))

        content = tk.Frame(self.root, bg="#f5f5f5")
        content.pack(fill=tk.BOTH, expand=True)

        tk.Frame(content, bg="#f5f5f5", height=1).pack(fill=tk.Y, expand=True)

        form = tk.Frame(content, padx=20, pady=10, bg="#f5f5f5")
        form.pack(fill=tk.X)

        def make_entry_row(parent, row, label_text, var, show=None):
            tk.Label(
                parent,
                text=label_text,
                font=("Helvetica", 12, "bold"),
                anchor="w",
                fg="#1a1a1a",
                bg="#f5f5f5",
            ).grid(row=row, column=0, sticky="w", pady=4)

            outer = tk.Frame(
                parent,
                highlightbackground="#888888",
                highlightthickness=2,
                bg="#888888",
            )
            outer.grid(row=row, column=1, pady=4, padx=(8, 0), sticky="ew")

            entry = tk.Entry(
                outer,
                textvariable=var,
                width=33,
                font=("Helvetica", 12),
                fg="#1a1a1a",
                bg="#ffffff",
                insertbackground="#1a1a1a",
                relief=tk.FLAT,
            )

            if show:
                entry.configure(show=show)

            entry.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)
            return entry

        MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        DAYS = [str(d) for d in range(1, 32)]

        import datetime as _dt
        current_year = _dt.datetime.now().year
        YEARS = [str(y) for y in range(current_year - 10, 1949, -1)]

        email_var = tk.StringVar()
        first_name_var = tk.StringVar()
        last_name_var = tk.StringVar()
        password_var = tk.StringVar()
        month_var = tk.StringVar(value=MONTHS[0])
        day_var = tk.StringVar(value=DAYS[0])
        year_var = tk.StringVar(value=YEARS[0])

        make_entry_row(form, 0, "Email:", email_var)
        make_entry_row(form, 1, "First Name:", first_name_var)
        make_entry_row(form, 2, "Last Name:", last_name_var)
        make_entry_row(form, 3, "Password:", password_var, show="*")

        tk.Label(
            form,
            text="Date of Birth:",
            font=("Helvetica", 12, "bold"),
            anchor="w",
            fg="#1a1a1a",
            bg="#f5f5f5",
        ).grid(row=4, column=0, sticky="w", pady=4)

        dob_frame = tk.Frame(form, bg="#f5f5f5")
        dob_frame.grid(row=4, column=1, pady=4, padx=(8, 0), sticky="w")

        month_menu = tk.OptionMenu(dob_frame, month_var, *MONTHS)
        month_menu.config(font=("Helvetica", 10), width=4)
        month_menu.pack(side=tk.LEFT, padx=(0, 4))

        day_menu = tk.OptionMenu(dob_frame, day_var, *DAYS)
        day_menu.config(font=("Helvetica", 10), width=3)
        day_menu.pack(side=tk.LEFT, padx=(0, 4))

        year_menu = tk.OptionMenu(dob_frame, year_var, *YEARS)
        year_menu.config(font=("Helvetica", 10), width=5)
        year_menu.pack(side=tk.LEFT, padx=(0, 4))

        def do_submit() -> None:
            email = email_var.get()
            first_name = first_name_var.get()
            last_name = last_name_var.get()
            password = password_var.get()

            day_str = day_var.get().zfill(2) if len(day_var.get()) == 1 else day_var.get()
            dob = f"{month_var.get()} {day_str}, {year_var.get()}"

            ok, msg = validate_registration(email, first_name, last_name, password, dob)
            if not ok:
                messagebox.showwarning("Registration", msg)
                return

            user = RegisterUser(
                email=email.strip(),
                firstName=first_name.strip(),
                lastName=last_name.strip(),
                password=password,
                dob=dob,
            )

            self._user_service.save_user(user)
            messagebox.showinfo("Registration", "Registration Successful")
            self.show_main_menu()

        def do_exit() -> None:
            self.show_main_menu()

        btn_frame = tk.Frame(content, bg="#f5f5f5")
        btn_frame.pack(pady=16)

        reg_btn_style = {
            "font": ("Helvetica", 12, "bold"),
            "width": 12,
            "height": 3,
            "relief": tk.RAISED,
            "cursor": "hand2",
            "borderwidth": 2,
            "highlightbackground": "#2c3e50",
            "fg": "#1a1a1a",
            "activeforeground": "#1a1a1a",
        }

        tk.Button(
            btn_frame,
            text="Submit",
            bg="#27ae60",
            activebackground="#219a52",
            command=do_submit,
            **reg_btn_style,
        ).pack(side=tk.LEFT, padx=8, pady=8)

        tk.Button(
            btn_frame,
            text="Exit",
            bg="#c0392b",
            activebackground="#a93226",
            command=do_exit,
            **reg_btn_style,
        ).pack(side=tk.LEFT, padx=8, pady=8)

        tk.Frame(content, bg="#f5f5f5", height=1).pack(fill=tk.Y, expand=True)

    def show_view_reservation(self) -> None:
        reservations = self._reservation_service.get_reservations_by_email(self.logged_in_email)

        if not reservations:
            messagebox.showinfo("View Reservations", "No reservations found.")
            return

        self.clear_window()

        tk.Label(
            self.root,
            text="Your Reservations",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#1a1a1a",
        ).pack(pady=(20, 10))

        container = tk.Frame(self.root, bg="#f5f5f5")
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        for i, reservation in enumerate(reservations, start=1):
            card = tk.Frame(
                container,
                bg="#ffffff",
                bd=1,
                relief=tk.SOLID,
                padx=10,
                pady=8,
            )
            card.pack(fill=tk.X, pady=6)

            details = (
                f"Reservation {i}\n"
                f"Days: {reservation.number_of_days}\n"
                f"From: {reservation.from_date}\n"
                f"To: {reservation.to_date}\n"
                f"Persons: {reservation.number_of_persons}\n"
                f"Rooms: {reservation.number_of_rooms}"
            )

            tk.Label(
                card,
                text=details,
                justify="left",
                anchor="w",
                font=("Helvetica", 11),
                bg="#ffffff",
                fg="#1a1a1a",
            ).pack(anchor="w")

        tk.Button(
            self.root,
            text="Back",
            bg="#95a5a6",
            activebackground="#7f8c8d",
            fg="#1a1a1a",
            activeforeground="#1a1a1a",
            command=self.show_user_menu,
            width=16,
            font=("Helvetica", 11, "bold"),
        ).pack(pady=15)

    def show_make_reservation(self) -> None:
        self.clear_window()

        tk.Label(
            self.root,
            text="Make Reservation",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#1a1a1a",
        ).pack(pady=(20, 12))

        tk.Label(
            self.root,
            text="Date format: YYYY-MM-DD",
            font=("Helvetica", 10),
            bg="#f5f5f5",
            fg="#333333",
        ).pack()

        form = tk.Frame(self.root, bg="#f5f5f5")
        form.pack(pady=10)

        days_var = tk.StringVar()
        from_date_var = tk.StringVar()
        to_date_var = tk.StringVar()
        persons_var = tk.StringVar()
        rooms_var = tk.StringVar()

        fields = [
            ("Number of Days:", days_var),
            ("From Date (YYYY-MM-DD):", from_date_var),
            ("To Date (YYYY-MM-DD):", to_date_var),
            ("Number of Persons:", persons_var),
            ("Number of Rooms:", rooms_var),
        ]

        for row, (label_text, variable) in enumerate(fields):
            tk.Label(
                form,
                text=label_text,
                bg="#f5f5f5",
                fg="#1a1a1a",
                font=("Helvetica", 11, "bold"),
            ).grid(row=row, column=0, sticky="w", padx=8, pady=6)

            tk.Entry(
                form,
                textvariable=variable,
                width=30,
            ).grid(row=row, column=1, padx=8, pady=6)

        def save_new_reservation():
            days = days_var.get().strip()
            from_date = from_date_var.get().strip()
            to_date = to_date_var.get().strip()
            persons = persons_var.get().strip()
            rooms = rooms_var.get().strip()

            if not all([days, from_date, to_date, persons, rooms]):
                messagebox.showerror("Error", "Please fill all reservation fields.")
                return

            if not days.isdigit():
                messagebox.showerror("Error", "Number of Days must be a whole number.")
                return

            if not persons.isdigit():
                messagebox.showerror("Error", "Number of Persons must be a whole number.")
                return

            if not rooms.isdigit():
                messagebox.showerror("Error", "Number of Rooms must be a whole number.")
                return

            try:
                from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
                to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Dates must be in YYYY-MM-DD format.")
                return

            if to_date_obj <= from_date_obj:
                messagebox.showerror("Error", "To Date must be after From Date.")
                return

            reservation = Reservation(
                email=self.logged_in_email,
                number_of_days=days,
                from_date=from_date,
                to_date=to_date,
                number_of_persons=persons,
                number_of_rooms=rooms,
            )

            self._reservation_service.save_reservation(reservation)
            messagebox.showinfo("Success", "Reservation saved successfully.")
            self.show_user_menu()

        tk.Button(
            self.root,
            text="Reserve",
            command=save_new_reservation,
            width=16,
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Back",
            command=self.show_user_menu,
            width=16,
        ).pack(pady=4)

    def show_cancel_reservation(self):

     reservation = self._reservation_service.get_reservation_by_email(self.logged_in_email)

     if reservation is None:
        messagebox.showinfo("Cancel Reservation", "No reservation found.")
        return

     confirm = messagebox.askyesno(
        "Cancel Reservation",
        "Are you sure you want to cancel your reservation?"
     )

     if not confirm:
        return

     self._reservation_service.delete_reservation(reservation)
     messagebox.showinfo("Cancel Reservation", "Reservation cancelled successfully.")
     self.show_user_menu()
    

    
    
    def show_modify_reservation(self) -> None:
        reservation = self._reservation_service.get_reservation_by_email(self.logged_in_email)

        if reservation is None:
            messagebox.showinfo("Modify Reservation", "No reservation found.")
            return

        self.clear_window()

        tk.Label(
            self.root,
            text="Modify Reservation",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#1a1a1a",
        ).pack(pady=(20, 12))

        tk.Label(
            self.root,
            text="Date format: YYYY-MM-DD",
            font=("Helvetica", 10),
            bg="#f5f5f5",
            fg="#333333",
        ).pack()

        form = tk.Frame(self.root, bg="#f5f5f5")
        form.pack(pady=10)

        days_var = tk.StringVar(value=reservation.number_of_days)
        from_date_var = tk.StringVar(value=reservation.from_date)
        to_date_var = tk.StringVar(value=reservation.to_date)
        persons_var = tk.StringVar(value=reservation.number_of_persons)
        rooms_var = tk.StringVar(value=reservation.number_of_rooms)

        fields = [
            ("Number of Days:", days_var),
            ("From Date (YYYY-MM-DD):", from_date_var),
            ("To Date (YYYY-MM-DD):", to_date_var),
            ("Number of Persons:", persons_var),
            ("Number of Rooms:", rooms_var),
        ]

        for row, (label_text, variable) in enumerate(fields):
            tk.Label(
                form,
                text=label_text,
                bg="#f5f5f5",
                fg="#1a1a1a",
                font=("Helvetica", 11, "bold"),
            ).grid(row=row, column=0, sticky="w", padx=8, pady=6)

            tk.Entry(
                form,
                textvariable=variable,
                width=30,
            ).grid(row=row, column=1, padx=8, pady=6)

        def save_modified_reservation():
            days = days_var.get().strip()
            from_date = from_date_var.get().strip()
            to_date = to_date_var.get().strip()
            persons = persons_var.get().strip()
            rooms = rooms_var.get().strip()

            if not all([days, from_date, to_date, persons, rooms]):
                messagebox.showerror("Error", "Please fill all reservation fields.")
                return

            if not days.isdigit():
                messagebox.showerror("Error", "Number of Days must be a whole number.")
                return

            if not persons.isdigit():
                messagebox.showerror("Error", "Number of Persons must be a whole number.")
                return

            if not rooms.isdigit():
                messagebox.showerror("Error", "Number of Rooms must be a whole number.")
                return

            try:
                from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
                to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Dates must be in YYYY-MM-DD format.")
                return

            if to_date_obj <= from_date_obj:
                messagebox.showerror("Error", "To Date must be after From Date.")
                return

            updated_reservation = Reservation(
                email=self.logged_in_email,
                number_of_days=days,
                from_date=from_date,
                to_date=to_date,
                number_of_persons=persons,
                number_of_rooms=rooms,
            )

            self._reservation_service.update_reservation(reservation, updated_reservation)
            messagebox.showinfo("Success", "Reservation updated successfully.")
            self.show_user_menu()

        tk.Button(
            self.root,
            text="Save Changes",
            command=save_modified_reservation,
            width=16,
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Back",
            command=self.show_user_menu,
            width=16,
        ).pack(pady=4)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = RestaurantReservationApp()
    app.run()
