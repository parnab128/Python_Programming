class Animal:
    def __init__(self, name):
        self.name=name
    def info(self):
        print("Animal name:", self.name)
class Dog(Animal):
    def sound(self):
        print(self.name, "says Meoowww...")
d=Dog("Tom")
# Inherited method
d.info()     
d.sound()