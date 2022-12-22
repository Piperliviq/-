class InvalidCommand(Exception):
    print("Invalid command!")
    pass

class InvalidAccountType(Exception):
    print("Invalid account type!")
    pass

class InvalidAccCurrency(Exception):
    def print(self):
        print("Invalid account currency!")
    pass

class UserNotFound(Exception):
    print("User not found!")
    pass

class AccNotFound(Exception):
    print("Account not found!")
    pass

class InvalidDataFormat(Exception):
    print("Invalid data format!")
    pass
