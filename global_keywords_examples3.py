# A python program to get a copy of global variable into a function and work with it:
# same name for global and local variables:
a=1 # this is global variable
def myfunction():
    a=2 # a is local variable
    x=globals()["a"] # get global variable into x
    print("global variable a= ", x) # Output: global variable a=  1
    print("local variable a= ", a) # Output: local variable a=  2
myfunction()
print("global variable a= ", a) # Output: global variable a=  1