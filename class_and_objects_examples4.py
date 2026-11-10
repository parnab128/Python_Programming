# A Python program to understand instance variables.
# instance vars example:
class Sample:
    # Constructor
    def __init__(self):
        self.x = 10
    # Instance method
    def modify(self):
        self.x += 1

# Create 2 instances
s1 = Sample()
s2 = Sample()
print("x in s1 =", s1.x) # Output: x in s1 = 10
print("x in s2 =", s2.x) # Output: x in s2 = 10
# Modify x in s1
s1.modify()
print("x in s1 =", s1.x) # Output: x in s1 = 11
print("x in s2 =", s2.x) # Output: x in s2 = 10