# 1. A Python program to create a text file to store individual characters :

# creating a file to store characters:
# open the file for writing data:
f=open('my.txt', 'w')
# enter characters from keyboard:
str=input("Enter Text: ")
# write the string into file:
f.write(str)
# closing the file:
f.close()