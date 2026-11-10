# ********** STATIC METHODS **********
# A python program to creat a static method that counts the number of instances created for a class:
# understanding static methods:
class myclass:
    # this is class var or static var:
    n=0
    # constructor that increments n when an instance is created
    def __init__(self):
        myclass.n=myclass.n+1
    # this is a static method to display the no. of instances
    @staticmethod
    def noObjects():
        print("No. of instances created: ", myclass.n)
# create 3 instances:
obj1=myclass()
obj2=myclass()
obj3=myclass()
myclass.noObjects()

# Output: No. of instances created:  3