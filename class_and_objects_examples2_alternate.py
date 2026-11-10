# A python program to define student class and creat an object to it. Also, we will call the method and display the student's details.
# instance variables and instance method:
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("Hi, I am", self.name)
        print("My age is", self.age)
        print("My marks are", self.marks)

s1 = Student("Vishnu", 20, 900)
s1.talk()