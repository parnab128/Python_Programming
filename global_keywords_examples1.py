# A python program to understand global and local variables:
# same name for global and local variables:
a=1 # this is global variable
def myfunction():
    a=2 # this is local variable
    print("a= ", a) # display local variable: a= 2
myfunction()
print("a= ", a) # display global variable: a= 1