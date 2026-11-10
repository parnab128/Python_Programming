# a python program to access each element of a string in forward and reverse orders using while loop:
if __name__ =="__main__":
    # indexing on strings:
    s1="Core Python"
    # access each character using while loop:
    n=len(s1) #n= no. of characters in string s1.
    i=0 # i=0,1,2,3,...,n-1.
    while i<n:
        print(s1[i], end=" ") # Output: C o r e   P y t h o n
        i=i+1
    print("\n") # put cursor into new line
    #  access in reverse order:
    i=-1 # Output: i=-1,-2,-3,...,-n.
    while i>=-n:
        print(s1[i], end=" ") # Output: n o h t y P   e r o C
        i=i-1
    print("\n") # put cursor into new line
    #  access in reverse order using negative index:
    i=1 # Output: i=1,2,3,...,n.
    while i<=n:
        print(s1[-i], end=" ") # Output: n o h t y P   e r o C
        i=i+1