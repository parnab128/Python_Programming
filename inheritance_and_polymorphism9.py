# A python program to override super class constructor and method in sub class.

# overriding the base class constructor and method in sub class :
class Father:
    def __init__(self):
        self.property=800000.00
    def display_property(self):
        print("Father\'s property= ", self.property)
class Son(Father):
    def __init__(self):
        self.property=200000.00
    def display_property(self):
        print("Child\'s property= ", self.property)
# create sub class instance and display father's property:
s=Son()
s1=Father()
s.display_property()
s1.display_property()