# A python program to define student class and creat an object to it. Also, we will call the method and display the student's details.
# instance variables and instance method:
class Student:
    # Constructor
    def __init__(self):
        self.name = "Vishnu"
        self.age = 20
        self.marks = 900

    # Instance method
    def talk(self):
        print("Hi, I am", self.name) # Output: Hi, I am Vishnu
        print("My age is", self.age) # Output: My age is 20
        print("My marks are", self.marks) # Output: My marks are 900

# Create an instance of Student class
s1 = Student()

# Call the method using the instance
s1.talk()