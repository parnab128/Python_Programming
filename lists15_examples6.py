# a python program to know how many times an elements occurred in the list:
if __name__ =="__main__":
    x=[] # take an empty list
    n=int(input("How many elements? ")) # accept input into n
    print("Enter elements: ")
    for i in range(n): # repeat for n times
        print(end="")
        x.append(int(input())) # add the elements to the list x
    print("The list is: ", x) # display the list
    y=int(input("Enter element to count: "))
    c=0
    for i in x:
        if(y==i): c=c+1
    print("{} is found {} times.".format(y, c))
        
        