# A python program to access global variable inside a function and modify it:
# accessing the global variable inside a function:
a=1 # this is global variable
def myfunction():
    global a # this is global variable
    print("global a= ", a) # display global variable: global a=  1
    a=2 # modify global value
    print("modified a= ", a) # display new value: modified a=  2
myfunction()
print("global a= ", a) # display modified value: global a=  2