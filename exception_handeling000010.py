# Program 10: A Python program to handle multiple exceptions:
# exception_handeling000010
# example for two exceptions:
# a function to find total and average of list elements:
def avg(list):
    tot=0
    for x in list:
        tot+=x
    avg=tot/len(list)
    return tot, avg
# call the avg() and pass a list
try:
    t,a=avg([1, 2, 3, 4, 5, "a"]) # here, give empty list and try.
    print("Total={}, Average={}".format(t,a))
except TypeError:
    print("Type Error, please provide numbers.")
except ZeroDivisionError:
    print("ZeroDivisionError, please do not give empty list.")