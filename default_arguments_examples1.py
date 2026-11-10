# a python program to understand the use of default arguments in a function.
# default arguments demo:
def grocery(item, price=40.00):
    """to display the given arguments"""
    print("Item=%s" %item)
    print("Price=%.2f" %price)
# call grocery() and pass 2 arguments:
grocery(item="Sugar", price=50.55) # pass 2 arguments
grocery(item="Sugar") # default value for price is used.

''' Output:
             Item=Sugar
             Price=50.55
             Item=Sugar
             Price=40.00
'''`