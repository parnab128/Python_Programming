# Program 5: A Python program to increment the salary of an employee by 15%:
# exception_handeling00005
# logical error:
def increment(sal):
    sal=sal*15/100
    return sal
# call increment() and pass salary
sal=increment(5000.00)
print("Incremented salary=%.2f" %sal)