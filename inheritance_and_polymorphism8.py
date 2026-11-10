# A python program to access the base class constructor from sub class.

# base class constructor is available to sub class:
class Father:
    def __init__(self):
        self.property=800000.00
    def display_property(self):
        print("Father\'s property= ", self.property)
class Son(Father):
    pass # we do not want to write anything in the sub class.
# create sub class instance and display father's property:
s=Son()
s.display_property() # Output: Father's property=  800000.0