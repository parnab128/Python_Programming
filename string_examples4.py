# a python program to access the characters of a string using for loop:
if __name__ =="__main__":
    # indexing on strings:
    s1="Core Python"
    # access each character using for loop:
    for i in s1:
        print(i, end=" ") # Output: C o r e   P y t h o n
    print("\n") # put cursor into new line
    #  access in reverse order:
    for  i in s1[::-1]:
        print(i, end=" ") # Output: n o h t y P   e r o C