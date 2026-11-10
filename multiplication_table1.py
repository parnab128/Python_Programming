if __name__ =="__main__":
    n=int(input("Enter any number: "))
    print("multiplication table of", n, "is:") 
    for i in range(1, 11, 1):  # 11 as 1 to 10
        k=n*i
        print(f"{n} x {i} = {k}")