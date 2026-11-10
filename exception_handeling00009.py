# Program 9: A Python program to handle IOError produced by open() function:
# exception_handeling00009
# example for IOError:
# accept a filename:
try:
    name=input("Enter filename: ")
    f=open(name, "r")
except IOError:
    print("File not found: ", name)
else:
    n=len(f.readlines())
    print(name, "has", n, "lines")
    f.close()