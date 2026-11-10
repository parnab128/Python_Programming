# ********** multilevel inheritance **********

class grand_father:
    def __init__(self, name, dob):
        self.name=name
        self.dob=dob
    def printf(self):
        print("Grand Father\'s name is= ", self.name)
        print("Grand Father\'s date of birth is= ",self.dob)

class father(grand_father):
    def __init__(self, name, dob, name1, dob1):
        super().__init__(name, dob)
        self.name1=name1
        self.dob1=dob1
    def show(self):
        print(self.name1, self.dob1)

class child(father):
    def __init__(self, name, dob, name1,dob1, name2, age):
        super().__init__(name, dob, name1, dob1)
        self.name2=name2
        self.age=age
    def printf1(self):
        print(self.name2, self.age)

# find name, dob, age:
a=child("Kali_Dadu", 69, "Kali_Baba", 39, "Kali", 10)
a.printf()
a.show()
a.printf1()