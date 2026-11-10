if __name__ =="__main__":
    # 1. Creating a list
    my_list=[1, 2, 3, 4, 5]
    print(my_list)# [1, 2, 3, 4, 5]

    # 2. List with different data types
    mixed_list=[10, "hello", 3.14, True]
    print(mixed_list)# [10, "hello", 3.14, True]

    # 3. Accessing elements
    numbers=[10, 20, 30, 40]
    print(numbers[0])   # first element 10
    print(numbers[-1])  # last element 40

    # 4. Adding elements
    fruits=["apple", "banana"]
    fruits.append("orange")   # add at end
    print(fruits)# ['apple', 'banana', 'orange']

    # 5. Removing elements
    colors=["red", "green", "blue"]
    colors.remove("green")
    print(colors)# ['red', 'blue']

    # 6. Loop through a list
    for item in ["a", "b", "c"]:
        print(item)#a
                   #b
                   #c
    # 7. List comprehension (short and powerful)
    squares=[x**2 for x in range(5)]
    print(squares) #[0, 1, 4, 9, 16]