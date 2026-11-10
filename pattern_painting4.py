if __name__ =="__main__":
    n=int(input("Enter value of n: "))
    for i in range (1, n, 1):
        for j in range (i, 0, -1):
            print(j,end=" ")
        print("\n")
    for i in range (n, 0, -1):
        for j in range (i, 0, -1):
            print(j,end=" ")
        print("\n")    
''' output is:
    1
    
    2 1
    
    3 2 1
    . . .
    
    . . .
    
    . . .
    
    ... 3 2 1
    
    ... 4 3 2 1
    
    ... 3 2 1
    
    . . .
    
    . . .
    
    . . .
    
    3 2 1
    
    2 1
    
    1                  '''