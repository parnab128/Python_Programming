# accessing the tuple elements:
if __name__ =="__main__":
    tup=(50, 60, 70, 80, 90, 100)
    print(tup[0]) # Output: 50
    print(tup[1]) # Output: 60
    print(tup[2]) # Output: 70
    print(tup[3]) # Output: 80
    print(tup[4]) # Output: 90
    print(tup[5]) # Output: 100
    print(tup[-1]) # Output: 100
    print(tup[-2]) # Output: 90
    print(tup[-3]) # Output: 80
    print(tup[-4]) # Output: 70
    print(tup[-5]) # Output: 60
    print(tup[-6]) # Output: 50
    print(tup[:]) # Output: (50, 60, 70, 80, 90, 100)
    print(tup[1:4]) # Output: (60, 70, 80) || to extract the elements from 1st to 4th.
    print(tup[-4:-1]) # Output: (70, 80, 90) || The elements from 4th to one element before the ending element(left to right) will be extracted.
    print(tup[::2]) # Output: (50, 70, 90) || Here, start and stop assume default values.
    print(tup[::-2) # Output: (100, 80, 60) || reverse order