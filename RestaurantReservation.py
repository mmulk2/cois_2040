from dataclasses import dataclass
@dataclass
class RegisterUser:
    # def __init__(self, email, firstName, lastName, __password, __dob, submit, Exit):
    #     self.email = email
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.__password = __password
    #     self.__dob = __dob
    #     self.submit = submit
    #     self.exit = Exit
    email: str
    firstName: str
    lastName: str
    __password: str
    __dob: str

    print("Registration in progress")

    def __str__(self):
        return f"""{self.firstName} | {self.lastName} | {self.email} """

    

if __name__ == "__main__":
    print("|====================================================|\n")
    print("|   Welcome to Some Restaurant Reservation System    |\n")
    print("|====================================================|\n")
    print("|    Please Select one of the following Options:     |\n")
    print("|                 1. Register/signup                 |\n")
    print("|                 2. Login                           |\n")
    print("|                 3. Exit                            |\n")
    print("|====================================================|\n")

    try:
        option = int(input("Enter option 1 or 2 or 3: "))
        if (option == 1):
            print("You have selected: Register/signup")
        elif (option == 2):
            print("")
        elif (option == 3):
            print("")
        else:
            raise ValueError("Number out of range")
    except ValueError as e:
        print(f"Invalid input: {e}")
        customer = RegisterUser()
            

