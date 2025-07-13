from functools import reduce
import sys

great70= lambda a: a>=70 and a<=90
add10=lambda a: a+10

def reducedata(no1,no2):
    return no1*no2

def main():
    #entering the number of items in a single line of input
    a=int(sys.argv[1])
    Data=[]
    for i in range (2,(a+2),1):
        no1=sys.argv[i]
        Data.append(int(no1))
    
    print("The dataset you enetered is:",Data)

    #data=[88,66,70,81,82,86,90]
    filterx=list(filter(great70,Data))
    print("the filtered data is:",filterx)
    mapx=list(map(add10,filterx))
    print("the mapped data is:",mapx)
    reducex=reduce(reducedata,mapx)
    print("the sum of data is:",reducex)

if __name__=="__main__":
    main()