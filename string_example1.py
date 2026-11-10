# 1. Creating Strings
str1 = 'Hello'# Using single quotes
str2 = "World"# Using double quotes
str3 = """This is
a multi-line
string."""# Using triple quotes (multi-line string)

# 2. Accessing Characters
text = "Python"
print(text[0])   # P
print(text[-1])  # n (last character)

# 3. String Slicing
text = "Python"
print(text[0:4])  # Pyth
print(text[2:])   # thon
print(text[:3])   # Pyt

# 4. String Concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Hello World

# 5. String Methods
text = "hello world"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.replace("world", "Python"))  # hello Python

# 6. String Formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")# f-string (recommended)
print("My name is {} and I am {} years old.".format(name, age))# format() method

# 7. from programmer
# String entered by user
user_string = input("Enter any string: ")
print("You entered:", user_string)
