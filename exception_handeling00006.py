# # Program 6: A Python program to understand the effect of an exception:
# exception_handeling00006
# an exception example
# open a file
f=open("myfile00001", "w")
# do some processing on the file
# accept a, b values, store the result of a/b into the file
a, b=[int(x) for x in input("Enter two numbers: ").split()]
c=a/b
f.write("writing %d into myfile" %c)
# close the file:
f.close()
print("File closed")