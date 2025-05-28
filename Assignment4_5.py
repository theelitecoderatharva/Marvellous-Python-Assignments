import sys
from functools import reduce

primechk= lambda a: a%2!=0
otherprimechk=lambda a: a==3 or a%3!=0
multi2=lambda a: a*2

def max(a,b):
    max=a
    for i in range(0,A,1):
        if max<b:
            max=b
        return max

def fmr(Data):
    filt2chkfunc=list(filter(primechk,Data))
    print("--------------")
    filt3chkfunc=list(filter(otherprimechk,filt2chkfunc))
    print("the filter data is:",filt3chkfunc)
    print("--------------")
    mapfunc=list(map(multi2,filt3chkfunc))
    print("the map data is:",mapfunc)
    print("--------------")
    redfunc=(reduce(max,mapfunc))
    print("the reduce data is:",redfunc)
    print("--------------")


def listprep():
    global A
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