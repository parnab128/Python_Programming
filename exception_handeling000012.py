# Program 12: A Python program using the assert statement and catching AssertionError:
# exception_handeling000012
# handling AssertionError:
try:
    x=int(input("Enter a number between 5 and 10: "))
    assert x>=5 and x<=10
    print("The number entered: ", x)
except AssertionError:
    print("The condition is not fulfilled")