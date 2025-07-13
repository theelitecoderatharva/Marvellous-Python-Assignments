import sys
from functools import reduce
def main():
    A=(lambda a,b:a*b)

    a=int(sys.argv[1])
    Data=[]
    for i in range(2,a+2,1):
        Data.append(int(sys.argv[i]))
    print("the entered data is:",Data)

    red=reduce(A,Data)
    print("the reduce list into product is:",red)

if __name__=="__main__":
    main()