if __name__ =="__main__":
    # a python program to add lists by loop:
    x=[10, 20, 30]
    y=[1, 2, 3, 4]
    lst=[]
    for i in x:
        for j in y:
            lst.append(i+j)
    print(lst)