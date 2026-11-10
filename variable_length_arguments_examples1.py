# a python program to show variable length argument and its use.
# variable length arguments demo:
def add(farg, *args): # *args can take 0 or more values || get a tuples.
    ''' to add given numbers'''
    print("Formal argument:", farg)
    sum=0
    for i in args:
        sum=sum+i
    print("Sum of all numbers:", (farg+sum))
# call add() and pass arguments:
add(5, 10) # after first argument, other values pass by tuple.
add(5, 10, 20, 30) # after first argument, other values pass by tuple.
''' Ouyput: 
Formal argument: 5
Sum of all numbers: 15
Formal argument: 5
Sum of all numbers: 65
'''