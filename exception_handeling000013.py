# Program 13: A Python program to use the assert statement with a message:
# exception_handeling000013
# handling AssertionError -v 2.0:
try:
    x=int(input("Enter a number between 5 and 10: "))
    assert x>=5 and x<=10, "Your input is not correct"
    print("The number entered: ", x)
except AssertionError as obj:
    print(obj)