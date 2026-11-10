# a python program to find maximum and minimum elements in a list of elements:
if __name__ =="__main__":
    x=[] # temporary list for input
    print("How many elements?", end="")
    n=int(input()) # accept input into n
    print("Enter elements: ")
    for i in range(n): # repeat for n times
        print(end="")
        x.append(int(input())) # add the element to the list x
    y=tuple(x) # convert list to tuple
    print("The tuple is: ", y) # display the list
    big=y[0]
    small=y[0]
    for i in range(0, len(x)):
        if y[i]>big:
            big=y[i]
        if y[i]<small:
            small=y[i]
    print("max is: ", big)
    print("min is: ", small)