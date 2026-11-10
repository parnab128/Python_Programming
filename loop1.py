if __name__ =="__main__":
# 1. For loop (basic)
    for i in range(5):
        print(i) # 0, 1, 2, 3, 4

# 2. For loop with a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit) # apple, banana, cherry

# 3. While loop
    count = 0
    while count < 5:
        print(count)
        count += 1

# 4. Loop with break   
    for i in range(10):
        if i == 5:
            break
        print(i)

# 5. Loop with continue 
    for i in range(5):
        if i == 2:
            continue
        print(i)

# 6. Nested loop
    for i in range(3):
        for j in range(2):
            print(i, j)