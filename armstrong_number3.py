if __name__ =="__main__":
    while True:
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
        a=input("Are you continued this process? press any key for yes and n for no.\n")
        if a == "n":
           break
