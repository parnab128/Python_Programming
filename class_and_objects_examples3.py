# A Python program to create a Student class with a constructor
# having more than one parameter, instance variables, and instance method.
class Student:
    # Constructor
    def __init__(self, n="", m=0):
        self.name = n
        self.marks = m

    # Instance method
    def display(self):
        print("Hi", self.name)
        print("Your marks", self.marks)

# Constructor is called without any arguments
s = Student()
s.display()
print("----------")
# Constructor is called with 2 arguments
name=input("Enter your name: ")
s1 = Student(name, 880)
s1.display()
print("----------")