# example of inheritance:
# single inheritance:
class A:
    name1="KALI LINUX"
    add="Name of the man?"
class B(A):
    name2="RAM"
    roll=85
    cls=9
    gender="male"
obj=B()
print(obj.name2) # Output: RAM
print(obj.roll) # Output: 85
print(obj.cls) # Output: 9
print(obj.gender) # Output: male
print(obj.name1) # Output: KALI LINUX
print(obj.add) # Output: Name of the man?
obj=A()
print(obj.name1) # Output: KALI LINUX
print(obj.add) # Output: Name of the man?