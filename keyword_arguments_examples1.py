# a python program to understand the keyword arguments of a function.
# keyword arguments demo:
def grocery(item, price):
    """to display the given arguments"""
    print("Item=%s" %item)
    print("Price=%.2f" %price)
# call grocery() and pass 2 arguments:
grocery(item="Sugar", price=50.55) # keyword arguments
grocery(price=90.65, item="oil") # keyword arguments