# Program 16: A Python program to store the messages released by any exception into a log file.:
# exception_handeling000016
# logging all messages from a program:
import logging
# store logging messages into log.txt file.
logging.basicConfig(filename="log.txt", level=logging.ERROR)
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    c=a/b
except Exception as e:
    logging.exception(e)
else:
    print("The result of division: ",c)