def factorialTail(n):
    # Base case
    if n==1 or n==0:
        return 1
    else:
        # Tail recursive call
        return n*factorialTail(n-1)
if __name__ == "__main__":
    a=int(input("enter which number's factorial you want?\n"))
    fact1=factorialTail(a)
    print("\nRecursive Factorial of", a, "is:", fact1);