if __name__ =="__main__":
    x=15.56
    print(type(x))
    print(type(int(x)))#not store in memory int(x)
    x=int(x)#store in memory and will display 15
    print(type(x))
    print("integer value is:",x)
    num=15
    print(type(num))
    num=float(num)#store in memory and will display 15.0
    print(type(num))
    print("floating value is:",num)
    n=19
    print(type(n))
    n=complex(n)#store in memory and will display 10+0j
    print(type(n))
    print("floating value is:",n)
    a=10
    b=-6
    d=complex(a,b)#store in memory and will display (10-6j)
    print("floating value is:",d)