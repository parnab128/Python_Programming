# a python program to sort the list elements using bubble sort technique:
if __name__ =="__main__":
    # sorting a list using bubble sort technique
    # create an empty list to store integers
    x = []
    # store elements into the list
    print("How many elements? ", end='')
    n = int(input())
    for i in range(n):      # repeat for n times
        print("Enter element: ", end='')
        x.append(int(input()))   # add the element to the list
    print("Original list: ", x)
    # bubble sort
    flag = False
    for i in range(n - 1):
        flag = False
        for j in range(n - 1 - i):
            if x[j] > x[j + 1]:
                # swap elements
                t = x[j]
                x[j] = x[j + 1]
                x[j + 1] = t
                flag = True
        if flag == False:
            break
        else:
            flag=False # assign initial value to flag
    print("Sorted list: ", x)