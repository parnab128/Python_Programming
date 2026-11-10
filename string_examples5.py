# a python program to access the characters of a string using for loop:
if __name__ =="__main__":
    s1="Game development"
    n=len(s1)
    print("The length of the string s1 is:", n)
    print("The range of the string s1 is, 0 to", n) # as in python range be before n, i.e, to n-1. But, in C language the range became 0 to <=15
    print(s1[1:4:1]) # Output: ame || firstly 1= start, secondly 4= stop before 4, thiredly 1= 1 step increment.
    print(s1[12:16:1]) # Output: ment
    print(s1[0:15:1]) # Output: Game developmen
    print(s1[0:16:1]) # Output: Game development
    print(s1[1:16:1]) # Output: ame development
    print(s1[1:16:2]) # Output: aedvlpet
    print(s1[1:16:4]) # Output: adle
    print(s1[1:16:6]) # Output: ave
    print(s1[1:16:8]) # Output: al
    print(s1[1:16:-4]) # Output: || here nothing is print because the assumption(case) became wrong.
    print(s1[::1]) # Output: Game development
    print(s1[::-1]) # Output: tnempoleved emaG
    print(s1[-1:16:-1]) # Output: || here nothing is print because the assumption(case) became wrong.
    print(s1[-1:-16:-4]) # Output: tpve
    print(s1[-1:-17:-1]) # Output: tnempoleved emaG
    print(s1[15:-1:-1]) # Output: || here nothing is print because the assumption(case) became wrong.