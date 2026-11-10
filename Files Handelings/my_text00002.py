# 2. A Python program to read characters from a text file :

# reading characters from file:
# open the file for reading data:
f=open('my00002.txt', 'r')
# read all characters from files:
str=f.read()
# display them on the screen:
print(str)
# closing the file:
f.close()