# you define a generator function exactlyn like a normal function, but you swap return for yield:
if __name__ =="__main__":
    # defining the generator function:
    def count_up_to(max_number):
        count=1
        while count<=max_number:
            yield count # pauses here and return the current count|
            count=count+1
    # creating the generator object
    counter=count_up_to(3)
    # consuming values using next()
    print(next(counter)) # Output: 1
    print(next(counter)) # Output: 2
    print(next(counter)) # Output: 3
    # calling next(counter) again would raise a StopIteration exception.
    print("\n")
    # another method:
    for num in count_up_to(3):
        print(num)