""" When a variable is decleared above a function,it becomes global variable.
Such variables are available to all the functions which are written after it.
Consider the following code: """
# global variable in a function:
a=1 # this is a global variable
def myfunction():
    b=2 # this is a local variable
    print("a=",a) # Display global variable
    print("b=",b) # Display local variable
myfunction()
print("value of a is: ", a) # available
print("value of b is: ", b) # ************ error, not available ************