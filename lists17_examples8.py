# a python program to find common elements in two lists:
if __name__ =="__main__":
    # Using a dictionary keyed by employee ID:
    emp=[] # take an empty list
    n = int(input("How many employees? ")) # accept input into n
    for i in range(n): # repeat for n times
        print("Enter id: ", end="")
        emp.append(int(input()))
        print("Enter name: ", end="")
        emp.append(input())
        print("Enter salary: ", end="")
        emp.append(float(input()))
    print("\nThe list is created with employee data.\n")
    print("search by list of employee data: ")
    id = int(input("Enter employee id: "))
    # display employee details upon taking id:
    for i in range(len(emp)):
        if id==emp[i]:
            print("Id= {:d}, Name= {:s}, Salary= {:.2f}".format(emp[i], emp[i+1], emp[i+2]))
            break