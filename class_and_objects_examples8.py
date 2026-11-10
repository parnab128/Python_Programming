# ********** INSTANCE METHOD **********
# A python program using a student class with instance methods to process the data of several students:
# instance methods to process data of the objects:
class student:
    # this is a constructor:
    def __init__(self, n="", m=0):
        self.name=n
        self.marks=m
    # this is an instance method:
    def display(self):
        print("Hi", self.name)
        print("Your marks", self.marks)
    # to calculate grades based on marks:
    def calculate(self):
        if(self.marks>=600):
            print("You got first grade.")
        elif(self.marks>=500):
            print("You got second grade.")
        elif(self.marks>=350):
            print("You got third grade.")
        else:
            print("You are failed.")
# create instances with some data from keyboard:
n=int(input("How many students? "))
i=0
while(i<n):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    # create student class instance and store data:
    s=student(name, marks)
    s.display()
    s.calculate()
    i=i+1
    print("--------------------")