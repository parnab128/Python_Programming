class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog says: Bow... Bow... Bow...")
class Cat(Animal):
    def speak(self):
        print("Cat says: Meow... Meow... Meow...")
class Hen(Animal):
    def speak(self):
        print("Hen says: Cluck... Cluck...")
class Cock(Animal):
    def speak(self):
        print("Cock says: Cock-a-doodle-doo...")
obj=Animal()
a=Dog()
d=Cat()
b=Hen()
c=Cock()
obj.speak()
a.speak()
b.speak()
c.speak()
d.speak()
