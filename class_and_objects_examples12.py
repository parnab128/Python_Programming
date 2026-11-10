# ********** STATIC METHODS **********
# A python program to creat a static method that calculates the square root value of a given number:
# a static method to find square root value:
import math
class sample:
    @staticmethod
    def calculate(x):
        result=math.sqrt(x)
        return result
# accept a number from keyboard:
num=float(input("Enter a number: "))
# call the static method and pass num:
res=sample.calculate(num)
print("The square root of {} is {:.2f}".format(num, res))