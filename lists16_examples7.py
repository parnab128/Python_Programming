# a python program to find common elements in two lists:
if __name__ =="__main__":
    # take two lists:
    a=["ram", "shyam", "jadu", "madhu"]
    b=["sita", "ram", "ganga", "madhu"]
    
    # convert them into sets:
    s1=set(a)
    s2=set(b)
    
    # find intersection:
    s3=s1.intersection(s2)
    
    # convert the resultant set into a list:
    common=list(s3)
    
    # display the list:
    print(common)