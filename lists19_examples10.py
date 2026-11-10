# a python program to retrieve elements from a matrix and display them:
if __name__ =="__main__":
    # take a nested list:
    mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Display the lists as it it is: ")
    print(mat)
    print("Display row by row: ")
    for r in mat:
        print(r)
    print("Display each column im row 0: ")
    for c in mat[0]:
        print("%d " %c, end="")
    print()
    print("Display each column im row 1: ")
    for c in mat[1]:
        print("%d " %c, end="")
    print()
    print("Display each column im row 2: ")
    for c in mat[2]:
        print("%d " %c, end="")
    print()
    print("Display all elements uning for: ")
    for r in mat:
        for c in r: # display column in each row:
            print(c, end=" ")
        print()
    print("Display all elements uning for: ")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("%d" %mat[i][j], end=" ")
        print()