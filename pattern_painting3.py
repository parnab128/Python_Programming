if __name__ =="__main__":
    n=int(input("Enter value of n: "))
    for i in range (1, n, 1):
        for j in range (i, 0, -1):
            print(j,end="")
        print()
    for i in range (n, 0, -1):
        for j in range (i, 0, -1):
            print(j,end="")
        print()    
''' output is:
    1
    21
    321
    . . .
    . . .
    . . .
    ...321
    ...4321
    ...321
    . . .
    . . .
    . . .
    321
    21
    1        '''