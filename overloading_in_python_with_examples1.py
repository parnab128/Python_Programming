# Overloading Examplea:

class A:
    def method(self, a=1, *args):
        total=0
        for i in args:
            total+=i
        return total+a
obj=A()
a=obj.method()
d=obj.method(10)
b=obj.method(2, 3)
c=obj.method(5, 6, 7)
print(a)
print(b)
print(c)
print(d)