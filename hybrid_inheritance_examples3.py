# Example 2: Hybrid Inheritance: School Education admitted persons in Python

class School:
    def persons(self):
        print("Person took admission: ")
class Boys(School):
    def only_boys(self):
        print("Only boys in Boys school.")
class Girls(School):
    def only_girls(self):
        print("Only girls in Girls school.")
class Coeducation(Boys, Girls):
    def boy_and_girls(self):
        print("Co-Ed. School admitted Both boys and girls.")
coeducation=Coeducation()
coeducation.persons()
coeducation.only_boys()
coeducation.only_girls()
coeducation.boy_and_girls()