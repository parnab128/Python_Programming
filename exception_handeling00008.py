# Program 8: A Python program to handle syntax error given by eval() function:
# exception_handeling00008
# example for syntax error:
try:
    date=eval(input("Enter date: "))
except SyntaxError:
    print("Invalid date entered")
else:
    print("You entered: ", date)
''' Enter date: 2016, 10, 03
    Invalid date entered
    
    Enter date: 2016, 10, 3
    You entered:  (2016, 10, 3)
    
    Enter date: 2016, 10b, 3
    Invalid date entered
'''