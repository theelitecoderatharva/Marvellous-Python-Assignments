import sys
from functools import reduce

greatorless= lambda a: 70<=a<=90
add=lambda a: a+10
product= lambda a,b: a*b

def fmr(Data):
    filtfunc=list(filter(greatorless,Data))
    print("the filter data is:",filtfunc)
    print("--------------")
    mapfunc=list(map(add,filtfunc))
    print("the map data is:",mapfunc)
    print("--------------")
    redfunc=(reduce(product,mapfunc))
    print("the reduce data is:",redfunc)
    print("--------------")


def listprep():
    A=int(sys.argv[1])
    D=list()
    u=0
    i=0
    for i in range(2,A+2,1):
        u=int(sys.argv[i])
        D.append(u)
    print(D)
    print("--------------")
    fmr(D)


if __name__=="__main__":
    listprep()