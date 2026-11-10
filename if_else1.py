# Print Numbers 0 to 6 Except 3 and 6
if __name__ =="__main__":
#  first method
    print("***** By first method *****")
    for i in range(7):
        if (i!=3 and i!=6):
            print(i,"\n")
#  second method
    print("***** By Second method *****")
    for i in range(7):
            if (i==3 or i==6):
                continue
            print(i,"\n")