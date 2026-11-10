if __name__ =="__main__":
    x=[1, 3, 5, 8, 9]
    y=[11, 13, 17, 19]
    print(x)
    print(y)
    print(x+y) # concatenate x and y  || output: [1, 3, 5, 8, 9, 11, 13, 17, 19]
    
    # Repetition of lists:
    print(x*2) # repeat the list x for 2 times  || output: [1, 3, 5, 8, 9, 1, 3, 5, 8, 9]
    
    # Membership in lists:
    a=3
    print(a in x) # check if a is member of x  ||  True
    print(a not in x) # check if a is not a member of x  ||  False
    
    # Aliasing and cloning lists:
    y=x # x is aliased as y
    print(x) # output: [1, 3, 5, 8, 9]
    print(y) # output: [1, 3, 5, 8, 9]