# Program 6: A Python program to know whether a file exists or not.

# checking if file exists and then reading data
import os, sys
# open the file for reading data
fname = input('Enter filename: ')
if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname + ' does not exist')
    sys.exit()
# read strings from the file
print('The file contents are: ')
str = f.read()
print(str)
# closing the file
f.close()
'''
C:\>python check.py
Enter filename: my00006.txt
The file contents are:
A Little Dream:-


The moon whispers softly to the night,
Stars shimmer gently with silver light.
Dreams drift quietly through the air,
Carrying wishes everywhere.
And when the morning paints the sky,
Hope wakes up and learns to fly.

C:\>python check.py
Enter filename: yourfile.txt
yourfile.txt does not exist
'''