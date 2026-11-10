# a python program to convert a string into key-value pairs and store them into a dictionary:
if __name__ =="__main__":
    # take a string:
    str="Viay=23, Ganesh=20, Lakshmi=19, Nikhil=22"
    # break the string at "," and then at "=":
    # store the pieces into a list lst:
    lst=[]
    print(lst) #  Output: []
    for x in str.split(","):
        y=x.split("=")
        lst.append(y)
        print(y) # Output: ['Viay', '23'] then line by line 
    print("\n",lst) #  Output: [['Viay', '23'], [' Ganesh', '20'], [' Lakshmi', '19'], [' Nikhil', '22']]
    # convert the list into dictionary "d":
    print("\n")
    # but this "d" will have both name and age as strings:
    d=dict(lst)
    print(d) # Output: {'Viay': '23', ' Ganesh': '20', ' Lakshmi': '19', ' Nikhil': '22'}