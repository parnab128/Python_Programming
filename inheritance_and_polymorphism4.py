# example of inheritance:
# single inheritance:
class A:
    name_f="lalu"
    number_f=123
class B(A):
    name_c="parnab"
    number_c=123456
obj=B()
print(obj.name_c) # Output: parnab
print(obj.number_c) # Output: 123456
print(obj.name_f) # Output: lalu
print(obj.number_f) # Output: 123
obj=A()
print(obj.name_f) # Output: lalu
print(obj.number_f) # Output: 123