# ********** INSTANCE METHODS **********
# A python program to create a Bank class where deposits and withdrawals can be handled by using instance methods.
# A class to handle deposits and withdrawals in a bank:
import sys
class Bank(object):
    """Bank related transactions"""
    # to initialize name and balance instance vars:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    # to add deposit amount to balance:
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    # to deduct withdrawal amount from balance:
    def withdraw(self, amount):
        if amount > self.balance:
            print("Balance amount is less, so no withdrawal.")
        else:
            self.balance -= amount
        return self.balance

# using the Bank class:
# create an account with the given name and balance 0.00:
name=input("Enter name: ")
b=Bank(name) # this is instance of Bank class.

# repeat continuously till choice is "e" or "E".
while(True):
    print("\nd - Deposit, w - Withdraw, e - Exit")
    choice=input("Your choice: ")
    if choice == 'e' or choice == 'E':
        sys.exit()
    # amount for deposit or withdraw:
    amt = float(input("Enter amount: "))
    # do the transaction:
    if choice == 'd' or choice == 'D':
        print("Balance after deposit:", b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print("Balance after withdrawal:", b.withdraw(amt))