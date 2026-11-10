# ********** CLASS METHODS **********
# A python program to use class method to handle the common feature of all the instances of Bird class:
# understanding class methods:
class Bird:
    # this is a class var:
    wings=2
    # this is a class method:
    @classmethod
    def fly(cls, name):
        print("{} flies with {} wings".format(name, cls.wings))
# display information for 2 birds:
Bird.fly("Sparrow")
Bird.fly("Pigeon")
'''
Output:
Sparrow flies with 2 wings
Pigeon flies with 2 wings
'''