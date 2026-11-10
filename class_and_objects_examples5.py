# ************ANOTHER METHOD***********class_and_objects_examples3**********

# A Python program to create a Student class with a constructor
# having more than one parameter, instance variables, and instance method.
class Student:
    # Constructor
    def __init__(self):
        pass
    def take(self):
        self.name = input("Enter Name: ")
        self.marks = int(input("Enter your marks: "))

    # Instance method
    def display(self):
        print("Hi", self.name)
        print("Your marks", self.marks)

# Constructor is called without any arguments
s = Student()
s.take()
s.display()
print("----------")
# Constructor is called with 2 arguments
s1 = Student()
s1.take()
s1.display()
print("----------")