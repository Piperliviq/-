from errors import *
class Account:
    def __init__(self, balance, currency, acc_type, IBAN):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

        if currency != "BGN" and currency != "EUR" and currency != "USD" and currency != "JPY":
            raise InvalidAccCurrency

        if acc_type != "Current" and acc_type != "Savings" and acc_type != "Credit":
            raise InvalidAccountType

    def print(self):
        return f"Account: {self.balance}, {self.currency}, {self.acc_type}, {self.IBAN}"

