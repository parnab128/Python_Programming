# a python program to creat a dictionary that does not change the order of elements:
if __name__ =="__main__":
    # creat an ordered dictionary:
    from collections import OrderedDict
    d=OrderedDict() # d is ordered dictionary
    d[65]="A"
    d[66]="B"
    d[67]="C"
    d[68]="D"
    d[69]="E"
    d[70]="F"
    d[71]="G"
    d[72]="H"
    d[73]="I"
    d[74]="J"
    d[75]="K"
    d[76]="L"
    d[77]="M"
    d[78]="N"
    d[79]="O"
    d[80]="P"
    d[81]="Q"
    d[82]="R"
    d[83]="S"
    d[84]="T"
    d[85]="U"
    d[86]="V"
    d[87]="W"
    d[88]="X"
    d[89]="Y"
    d[90]="Z"
    # display the ordered dictionary:
    for i, j in d.items():
        print(i, "--", j)