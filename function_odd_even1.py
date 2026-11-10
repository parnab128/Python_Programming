def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
if __name__ == "__main__":
    a=int(input("Enter any number: "))
    print(evenOdd(a))