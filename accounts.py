import datetime
import pytz


class Account:
    """Simple account class with a balance"""

    @staticmethod
    def _current_time(): # starting underscore informs not to use this method outside of the class
        utc_time = datetime.datetime.utcnow() # _blah_blah is only for internal use only
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance): # init method initializes a class & give value to data attributes
        self._name = name # always use self 
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for {} with a balance of {} ".format(self._name, self.__balance))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))  #showing negative amount
        else:
            print("The amount must be greater than zero and no more than your actual balance")
        self.show_balance()
    
    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= - 1
            print("{:6} {} on {} local time was {}".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    bruno = Account("Bruno", 0) # initiating the object bruno under the class Account
    bruno.show_balance()
    bruno.deposit(1000)
    bruno.withdraw(200)
    bruno.show_transactions() 
    bruno.show_balance()  # expected balance: 800
    bruno.withdraw(2000) # expect balance: -1200
    bruno.show_balance()
    bruno.show_transactions()
    
    steph = Account("Steph", 0) 
    steph.deposit(1000)
    steph.withdraw(200)
    steph.show_transactions()

    print(steph.__dict__)