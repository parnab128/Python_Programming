# 3. A Python program to store a group of strings into a text file :

# creating a file with strings:
# open the file for writing data:
f=open('my00003.txt', 'w')
# enter strings from keyboard:
print("Enter Text (@ at end): ")
while str!='@':
    str=input() # accept string into str
    # write the string into file:
    if(str!='@'):
        f.write(str+"\n")
# closing the file:
f.close()