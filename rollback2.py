
from decimal import *

class Account(object):
    _qb = Decimal('0.00') # class contant, accessible without creating an instance

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance # underscore indicates not to manually change value
        print("Account created for {}.".format(self.name), end='')
        self.show_balance()
    
    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print("{} deposited".format(amount))
        return self._balance
    
    def withdrawl(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{} withdrawn".format(amount))
            return amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0
        
    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))

if __name__ == '__main__':
    john = Account("John")
    john.deposit(10.10)
    john.deposit(.10)
    john.deposit(0.30)
    john.deposit(.10)
    john.withdrawl(0)
    john.show_balance()

        