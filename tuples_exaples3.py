if __name__ =="__main__":
    student=(10, "Vinay Kumar", 70, 73, 88, 91, 83)
    roll_no, name=student[0:2]
    print(roll_no) # Output: 10
    print(name) # Output: Vinay Kumar
    marks=student[2:7] # store the elements from 2nd to 6th into 'marks'.
    # tuple:
    for i in marks:
        print(i)
    '''# Output: 70
                 73
                 88
                 91
                 83'''