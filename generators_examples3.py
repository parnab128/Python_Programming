# squares of 0 to 1000000:
if __name__ =="__main__":
    # a list comprehension(loads everything into memory immediately)
    squares_list=[x**2 for x in range(1000000)]
    # a generator expression(comutes values on the fly, memory-efficient)
    squares_gen=(x**2 for x in range(1000000))
    print(next(squares_gen)) # Output: 0
    print(next(squares_gen)) # Output: 1
    print(next(squares_gen)) # Output: 4
    print(next(squares_gen)) # Output: 9