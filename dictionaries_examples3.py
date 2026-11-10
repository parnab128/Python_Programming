# a python program to show the usage of for loop to retrieve elements of dictionaries:
if __name__ =="__main__":
    # take a dictionary:
    colors={
    "r":"Red",
    "g":"Green",
    "b":"Blue",
    "w":"White"
    }
    # display only keys:
    for k in colors:
        print(k)

    # display only keys:
    for k in colors:
        print(colors[k])

    # items() method returns key and value pair into k, v:
    for k, v in colors.items():
        print("key={} value={}". format(k, v))