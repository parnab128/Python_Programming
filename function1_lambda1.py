# A lambda function in Python is a small anonymous function written in a single line using the lambda keyword.
# syntax:- lambda arguments: expression
if __name__ == "__main__":
    # Example 1: Simple Lambda
    square = lambda x: x * x
    print(square(5))
    '''Equivalent normal function:
    def square(x):
        return x * x'''
    # Example 2: Multiple Arguments
    add = lambda a, b: a + b
    print(add(3, 7))
    # Common Uses of Lambda Functions:-
    # 1. With map()
    numbers = [1, 2, 3, 4]
    result = list(map(lambda x: x * 2, numbers))
    print(result) # Output: [2, 4, 6, 8]
    # 2. With filter()
    numbers = [1, 2, 3, 4, 5, 6]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(even) # Output: [2, 4, 6]
    # 3. With sorted()
    students = [
        ("Alice", 85),
        ("Bob", 75),
        ("Charlie", 95)
    ]
    sorted_students = sorted(students, key=lambda x: x[1])
    print(sorted_students)
    # Output: [('Bob', 75), ('Alice', 85), ('Charlie', 95)]