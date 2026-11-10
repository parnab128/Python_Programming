if __name__ =="__main__":
    n=int(input("Enter the size of array: "))
    arr=[] # initialize an empty list
    for i in range(n):
        val = int(input(f"Enter the value at index {i}: "))
        arr.append(val)  # add value to the list
    for i in range(n):
        if arr[i]%2==0:
            print(arr[i], "is an even number\n")
        else:
            print(arr[i], "is an odd number\n")