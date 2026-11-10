# A python program to understand class variables or static variables:
# class vars or static vars example:
class sample:
    # this is a class var
    x=10
    # this is a class method
    @classmethod
    def modify(cls):
        cls.x+=1
# creat 2 instances:
s1=sample()
s2=sample()
print("x in s1= ",s1.x) # Output: x in s1=  10
print("x in s2= ",s2.x) # Output: x in s2=  10
# modify x in s1:
s1.modify()
print("x in s1= ",s1.x) # Output: x in s1=  11
print("x in s2= ",s2.x) # Output: x in s2=  11