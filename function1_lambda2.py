if __name__ == "__main__":
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    add = lambda a, b: a + b
    print("Addition of", a, "and", b, "is:", add(a, b))