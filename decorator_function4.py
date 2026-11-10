# a python program to creat two decorators to the same function using @ symbol:
# a decorator that increments the value of a function by 2
def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner
# a decorator that doubles the value of a function
def decor1(fun):
    def inner():
        value=fun()
        return value*2
    return inner
# take a function to which decorator should be applied
@decor
@decor1
def num():
    return 10
# callnum() function and apply decor1 and then decor
print(num())