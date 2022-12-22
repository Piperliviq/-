from errors import *
class User:
    def __init__(self, account, names, EGN):
        self.account = account
        self.names = names
        self.ENG = EGN

        if EGN != str(10):
            raise InvalidDataFormat

    def print(self):
        return f"User: {self.account}, {self.names}, {self.ENG}"