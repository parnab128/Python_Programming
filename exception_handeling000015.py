# Program 15: A Python program that creates a log file with errors and critical messages.:
# exception_handeling000015
# understanding logging of error messages:
import logging
# store messages into my log.txt file.
# store only the messages with level equal to or more than that of ERROR
logging.basicConfig(filename="mylog.txt", level=logging.ERROR)
# these messages are stored into the file.
logging.error("There is an error in the program.")
logging.critical("There is a problem in the design.")
# but these are not stored.
logging.warning("The project is going slow.")
logging.info("You are a junior programmer.")
logging.debug("Line no. 10 contains syntax error.")