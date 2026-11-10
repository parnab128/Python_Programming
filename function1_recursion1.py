def nsum(n):
    # Base condition to terminate the recursion when n = 0
    if n==0:
        return 0
    # Recursive case / recursive call
    res=n+nsum(n-1)
    return res
if __name__ == "__main__":
    # Calling the function
    a=int(input("enter how much number of first natural number: "))
    total=nsum(a)
    print("\nsum of first", a, "natural number is: ", total)
    