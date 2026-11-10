# a python program to understand keyword variable argument.

# PROCESS: 1

# keyword variable arguments demo:
def display(farg, **kwargs): # **kwarg can take 0 or more values
    ''' to display given values'''
    print("Formal argument=", farg)
    for x, y in kwargs.items(): # items() will give pairs of items
        print('key={}, value={}'.format(x, y))
# pass 1 formal arguments and 2 keyword arguments
display(5, rno=10)
print()
# pass 1 formal argument and 4 keyword arguments
display(5, rno=10, name="Parnab")