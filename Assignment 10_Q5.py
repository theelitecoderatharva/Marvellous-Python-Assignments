from functools import reduce
import sys


multi2=lambda a: a*2

def primechk(no):
    if no>1:
        if no==3 or no==2:
            return True
        elif(no%2!=0 and no%3!=0 and no%11!=0):
            return True
    else:
        return False


def reducedata(no1,no2):
    max=no1
    if no1<no2:
        max=no2
    return max

def main():
    #entering the number of items in a single line of input
    a=int(sys.argv[1])
    Data=[]
    for i in range (2,(a+2),1):
        no1=sys.argv[i]
        Data.append(int(no1))
    
    print("The dataset you enetered is:",Data)

    #data=[88,66,70,81,82,86,90]
    filterx=list(filter(primechk,Data))
    print("the filtered data is:",filterx)
    mapx=list(map(multi2,filterx))
    print("the mapped data is:",mapx)
    reducex=reduce(reducedata,mapx)
    print("the sum of data is:",reducex)

if __name__=="__main__":
    main()