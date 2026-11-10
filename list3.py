if __name__ =="__main__":
    a=[890,620,'Parnab',10.8862,True]
    print("First method")
    for i in range (5):
        print(a[i])
    ''' 890
        620
        Parnab
        10.8862
        True     '''
    print("\nSecond method")
    for item in a:
        print(item)
    ''' 890
        620
        Parnab
        10.8862
        True     '''
    print("\nThird method")
    for i in range (5):
        print(a[i], end=" ") # Output: 890 620 Parnab 10.8862 True
    print("\nFourth method")
    c=len(a)
    for i, item in enumerate(a):
        if i<c-1:
            print(item, end=", ")
        else:
            print(item)
    # Output: 890, 620, Parnab, 10.8862, True
    print("\nFifth method")
    print(*a, sep=", ") # Output: 890, 620, Parnab, 10.8862, True