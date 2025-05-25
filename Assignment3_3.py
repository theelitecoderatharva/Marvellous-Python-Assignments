def main():
    no1=int(input("enter the number of items you wnat"))
    Data=[]

    for i in range(1,no1+1,1):
        i=int(input())
        Data.append(i)
    print("The List you prepared is:",Data)


def Max(A):
    mini=A[0]
    for i in range(0,len(A),1):
        if A[i]<mini:
            mini=A[i]
    print("The smallest value of the Data is:",mini)


if __name__=="__main__":
    main()