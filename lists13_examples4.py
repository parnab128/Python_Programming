# a python program to find maximum and minimum elements in a list of elements:
if __name__ =="__main__":
    x=[] # take an empty lists
    print("How many elements?", end="")
    n=int(input()) # accept input into n
    print("Enter elements: ")
    for i in range(n): # repeat for n times
        print(end="")
        x.append(int(input())) # add the element to the list x
    print("The list is: ", x) # display the list
    big=x[0]
    small=x[0]
    for i in range(0, len(x)):
        if x[i]>big: big=x[i]
        if x[i]<small: small=x[i]
    print("max is: ", big)
    print("min is: ", small)