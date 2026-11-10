# ********** INSTANCE METHOD **********
# A python program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods:
# accessor and mutator methods:
class student:
    # mutator method
    def setName(self, name):
        self.name=name
    # accessor method
    def getName(self):
        return self.name
    # mutator method
    def setMarks(self, marks):
        self.marks=marks
    # accessor method
    def getMarks(self):
        return self.marks
# create instances with some data from keyboard:
n=int(input("How many student? "))
i=0
while(i<n):
    # create student class instance:
    s=student()
    name=input("Enter name: ")
    s.setName(name)
    marks=int(input("Enter marks: "))
    s.setMarks(marks)
    # retrieve data from student class instance:
    print("Hi", s.getName())
    print("Your marks", s.getMarks())
    i=i+1
    print("---------------------")