if __name__ =="__main__":
    # a python program of tuples:
    tup1=() # empty tuple
    tup2=(10,) # tuple with one element. Observe comma"," after the element.
    tup3=(10, 20, -30.2, 40.5, "Hydrabad", "New Delhi")
    tup4=(10, 20, 30) # tuples with integers
    tup5=1, 2, 3, 4, 5 # no braces
    print(tup1)
    print(tup2)
    print(tup3)
    print(tup4)
    print(tup5)
    
# *** list to tuple ***
    list=[1, 2, 3] # take a list
    tpl=tuple(list) # convert list into tuple
    print(tpl) # Display: tuple (1, 2, 3)

# creat a program from 4 to 8 in steps of 2
    tpl1=tuple(range(4, 9, 2)) # numbers from 4 to 8 in steps of 2
    print(tpl1) # Output: (4, 6, 8)