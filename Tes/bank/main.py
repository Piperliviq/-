from entities.Account import Account
from entities.bank import Bank
from entities.errors import *
from entities.User import User

class Menu:
    user_list = []

    def __init__(self, users):
        self.users = users

    def run(self):
        while True:
            self.print_menu()
            option = int(input("Choose options from the menu: \n "))
            if option == 7:
                break
            else:
                raise InvalidAccountType


    def print_menu(self):
        print("<<<<<<<<<MENU>>>>>>>>>")
        print("Option 1: Create user")
        print("Option 2: Create account for user")
        print("Option 3: List users")
        print("Option 4: List account for user")
        print("Option 5: Deposit for user")
        print("Option 6: Withdrawal for user")
        print("Option 7: Exit")

    def CreateUser(self):
        name = input("Enter the name of the User")
        EGN = input("Enter the user's EGN")


    def CreateNewAccount(self):
        user_name = input("Enter the name of the account")


