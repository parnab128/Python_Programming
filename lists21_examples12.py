if __name__ =="__main__":
    # a python program to square s of integers from 1 to 10 by lists:
    squares=[x**2 for x in range(1, 11)]
    print(squares)
    squares=[]
    for x in range(1, 11): # repeat x values from 1 to 10
        squares.append(x**2) # add squares of x to the list
    print(squares)
    
    # even squares:
    even_squares=[x**2 for x in range(1, 11) if x%2==0]
    print(even_squares)
    even_squares=[x**2 for x in range(2, 11, 2)]
    print(even_squares)