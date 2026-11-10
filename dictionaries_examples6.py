# a python program to accept a dictionary and display its elements:
if __name__ =="__main__":
    # a function that takes a dictionary as parameter:
    def fun(dictionary):
        for i, j in dictionary.items():
            print(i, "--", j)
    # take a dictionary:
    d={
    "a":"Apple",
    "b":"Book",
    "c":"Cat",
    "d":"Dog"
    }
    # call the function and pass the dictionary:
    print("\n", d) # Output: {'a': 'Apple', 'b': 'Book', 'c': 'Cat', 'd': 'Dog'}
    fun(d)
    ''' a -- Apple
        b -- Book
        c -- Cat
        d -- Dog
        '''