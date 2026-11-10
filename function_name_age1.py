def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)
if __name__ == "__main__":
    a=input("Enter your name: ")
    b=int(input("Enter your age: "))
    print("Case-1:")
    nameAge(a, b)
    ''' Case-1:
    Hi, I am a
    My age is b'''
    print("Case-2:")
    nameAge(b, a)
    ''' Case-1:
    Hi, I am b
    My age is a'''