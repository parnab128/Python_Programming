# Program 14: A Python program to create our own exception and raise it when needed.:
# exception_handeling000014
# create our own class as sub class to Exception class:
class MyException(Exception):
    def __init__(self, arg):
        self.msg = arg
    def __str__(self):
        return self.msg
# write code where exception may raise
# to raise the exception, use raise statement
def check(dict):
    for k, v in dict.items():
        print("Name= {:15s} Balance= {:10.2f}".format(k,v))
        if(v<2000.00):
            raise MyException("Balance amount is less in the account of"+k)
# our own exception is handeled using try and except blocks
bank= {"Raj":5000.00, "Vani":8900.50, "Ajay":1990.00, "Naresh":3000.00}
try:
    check(bank)
except MyException as me:
    print(me)