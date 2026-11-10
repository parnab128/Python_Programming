# a python program to add two matrices and display the sum matrix using lists:
if __name__ =="__main__":
    # nested lists - matrix addition:
    # take matrix one with 3 rows and 4 columns:
    m1=[ [1, 2, 3, 0],
         [4, 5, 6, 0],
         [7, 8, 9, 0] ]
    # take matrix one with 3 rows and 4 columns:
    m2=[ [1, 2, 3, 4],
         [1, 0, 1, 0],
         [2, -1, -2, 1] ]
         
    # # take matrix one with 3 rows and 4 columns and initialize with all 0s:
    m3=[4*[0] for i in range(3)] # repeat four 0s for 3 times
    
    # add the corresponding elements of m1 and m2 and store into m3
    for i in range(3):
        for j in range(4):
            m3[i][j]=m1[i][j]+m2[i][j]

    # display the third matrix using for loop
    for i in range(3):
        for j in range(4):
            print("%d" %m3[i][j], end=" ")
        print()