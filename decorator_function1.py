# a python program to demonstrate how decorate functions:
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper
@decorator
def greet():
    print("Hello, World!")
if __name__ =="__main__":
    greet()
''' Output:
            Before calling the function.
            Hello, World!
            After calling the function.
'''