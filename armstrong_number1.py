if __name__ =="__main__":
    n=int(input("Write a number: "))
    i=0
    arm=0
    p=n
    while n!=0:
        r=n%10
        arm=arm+r*r*r
        n=n//10#integer division
    if p==arm:
        print("This is an armstrong number.")
    else:
        print("This is not an armstrong number.")                                              