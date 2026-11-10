# Basic operations on tuples:
if __name__ =="__main__":
    student=(10, "Vinay Kumar", 70, 73, 88, 91, 83)
    a=len(student)
    print("length is: ", a) # Output: length is:  7
    fees=(25000.00,)*4 # repeat the tuples elements for 4 times.
    print(fees) # (25000.0, 25000.0, 25000.0, 25000.0
    student1=student+fees
    print(student1) # Output: (10, 'Vinay Kumar', 70, 73, 88, 91, 83, 25000.0, 25000.0, 25000.0, 25000.0)
    name="Vinay Kumar" # to know if this is member of student1 or not.
    b=name in student1
    print(b) # Output: True
    tpl=(10, 11, 12)
    tpl1=tpl*3 # repeat for 3 times and store in tpl1
    print(tpl1) # Output: (10, 11, 12, 10, 11, 12, 10, 11, 12)