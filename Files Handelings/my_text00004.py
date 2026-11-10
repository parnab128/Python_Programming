# 4. A Python program to read all the strings from the text file and display them :

# reading strings from a file:
# open the file for reading data:
f=open('my00004.txt', 'r')
# read strings from the file:
print("The file contents are: ")
str=f.read()
print(str)
# closing the file:
f.close()