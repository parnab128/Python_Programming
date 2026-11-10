""" When a variable is decleared above a function,it becomes global variable.
Such variables are available to all the functions which are written after it.
Consider the following code: """
# local variable in a function:
def myfunction():
    a=1 # this is a local variable
    a=a+1 # increment it
    print(a) # Output: 2
myfunction()
print("value of a is: ",) # ************ error, not available ************