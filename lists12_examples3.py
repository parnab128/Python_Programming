# fining biggest and smallest elements in a list:
if __name__ =="__main__":
    x=[1, 3, 5, 8, 9]
    n1=max(x)
    n2=min(x)
    print("big is: ", n1)
    print("small is: ", n2)
    
    # another process:
    big=x[0]
    small=x[0]
    for i in range(0, len(x)):
        if x[i]>big: big=x[i]
        if x[i]<small: small=x[i]
    print("max is: ", big)
    print("min is: ", small)