if __name__ =="__main__":
    n=int(input("Enter value of n, write it in odd number, n: "))
    for i in range (1, n+1, 1):
        print(" "*(n-i), end="")
        for j in range (i, 0, -1):
            print(j,end="")
        for j in range (2, i+1, 1):
            print(j,end="")
        print()
    for i in range (n-1, 0, -1):
        print(" "*(n-i), end="")
        for j in range (i, 0, -1):
            print(j,end="")
        for j in range (2, i+1, 1):
            print(j,end="")
        print()    
''' output is:
    ...1...
    ..212..
    .32123.
    . . . .
    . . . .
    . . . .
    .32123.
    ..212..
    ...1...         '''