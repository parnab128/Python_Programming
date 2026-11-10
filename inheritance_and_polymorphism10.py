# A python program to call the super class constructor in the sub class using super().

# accessing base class constructor in sub class :
class Father:
    def __init__(self, property=0):
        self.property=property
    def display_property(self):
        print("Father\'s property= ", self.property)
class Son(Father):
    def __init__(self, property1=0, property=0):
        super().__init__(property)
        self.property1=property1
    def display_property(self):
        print("Total property of child= ", self.property1+self.property)
# create sub class instance and display father's property:
a, b=[float(property) for property in input("Enter two property values: ").split()]
s=Son(a, b)
s.display_property()