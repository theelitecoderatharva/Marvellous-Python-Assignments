def main():
    no1=int(input("enter the number of items you wnat"))
    Data=[]

    for i in range(1,no1+1,1):
        i=int(input())
        Data.append(i)
    print("The List you prepared is:",Data)
    Max(Data)

def Max(A):
    large=0
    for i in range(0,len(A),1):
        if A[i]>large:
            large=A[i]
    print("The largest value of the Data is:",large)

if __name__=="__main__":
    main()