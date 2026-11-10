# a python program to apply a decorator to a function using @ symbol:
def decor(fun): # this is decorator function
    def inner(): # this is the inner function that modifies
        value=fun()
        return value+2
    return inner # return inner function
# take a function to which decorator should be applied
@decor # apply decor to the below function
def num():
    return 10
# call num() function and display its result
print(num())