# # Program 7: A Python program to handle the ZeroDivisionError exception:
# exception_handeling00007
# an exception handling example
try:
    f=open("myfile00002", "w")
    a, b=[int(x) for x in input("Enter two numbers: ").split()]
    c=a/b
    f.write("writing %d into myfile00002" %c)
except ZeroDivisionError:
    print("Division by zero happened")
    print("Please do not enter 0 in input")
finally:
    f.close()
    print("File closed")
''' Enter two numbers: 10 2
    File closed
    
    Enter two numbers: 10 0
    Division by zero happened
    Please do not enter 0 in input
    File closed
'''