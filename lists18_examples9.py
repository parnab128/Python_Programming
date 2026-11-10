# a python program to create a nested list and display its elements:
if __name__ =="__main__":
    list=[10,20, 30, 40, [80, 90]]
    print("Total list= ", list) # display entire list
    print("First element= ", list[0]) # display first element
    print("Last element is nested list= ", list[4]) # display nested list
    for x in list[4]: # display all elements in nested list
        print(x)