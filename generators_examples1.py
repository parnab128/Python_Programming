# To create a generator function, you use the def keyword and include one or more yield statements. Here's a simple example:
if __name__ =="__main__":
    def simple_generator():
       yield 1
       yield 2
       yield 3
    # Using the generator
    for value in simple_generator():
       print(value)

    gen_exp = (x * x for x in range(5))
    for value in gen_exp:
       print(value)