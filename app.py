"""
Main application controller - Tkinter GUI for Restaurant Reservation System.
Uses models, validators, and UserService following OOP separation of concerns.
"""

import tkinter as tk
from tkinter import messagebox

from models import RegisterUser
from user_service import UserService
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
            command=self.root.quit,
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
            email = email_var.get()
            password = password_var.get()
            if not (email and email.strip()):
                messagebox.showwarning("Login", "Please enter your email.")
                return
            if not (password and password.strip()):
                messagebox.showwarning("Login", "Please enter your password.")
                return
            if self._user_service.verify_login(email, password):
                self.logged_in_email = email.strip()
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

        def placeholder(name: str):
            def f():
                messagebox.showinfo(name, f"{name} functionality can be added here.")

            return f

        tk.Button(
            btn_frame,
            text="View Reservation",
            bg="#3498db",
            activebackground="#2980b9",
            command=placeholder("View Reservation"),
            **btn_style,
        ).pack(pady=6)
        tk.Button(
            btn_frame,
            text="Make Reservation",
            bg="#2ecc71",
            activebackground="#27ae60",
            command=placeholder("Make Reservation"),
            **btn_style,
        ).pack(pady=6)
        tk.Button(
            btn_frame,
            text="Modify Reservation",
            bg="#9b59b6",
            activebackground="#8e44ad",
            command=placeholder("Modify Reservation"),
            **btn_style,
        ).pack(pady=6)
        tk.Button(
            btn_frame,
            text="Cancel Reservation",
            bg="#e67e22",
            activebackground="#d35400",
            command=placeholder("Cancel Reservation"),
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

        email_var = tk.StringVar()
        first_name_var = tk.StringVar()
        last_name_var = tk.StringVar()
        password_var = tk.StringVar()
        dob_var = tk.StringVar()

        make_entry_row(form, 0, "Email:", email_var)
        make_entry_row(form, 1, "First Name:", first_name_var)
        make_entry_row(form, 2, "Last Name:", last_name_var)
        make_entry_row(form, 3, "Password:", password_var, show="*")
        make_entry_row(form, 4, "Date of Birth:", dob_var)

        def do_submit() -> None:
            email = email_var.get()
            first_name = first_name_var.get()
            last_name = last_name_var.get()
            password = password_var.get()
            dob = dob_var.get()

            ok, msg = validate_registration(
                email, first_name, last_name, password, dob
            )
            if not ok:
                messagebox.showwarning("Registration", msg)
                return

            user = RegisterUser(
                email=email.strip(),
                firstName=first_name.strip(),
                lastName=last_name.strip(),
                password=password,
                dob=dob.strip(),
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

    def run(self) -> None:
        self.root.mainloop()
