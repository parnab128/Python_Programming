# Program 11: A Python program to understand the usage of try with finally blocks:
# exception_handeling000011
# try without except block:
try:
    x=int(input("Enter a number: "))
    y=1/x
finally:
    print("We are not catching the exception.")
print("The inverse is: ", y)