def main():
    no1=int(input("enter the number of items you wnat"))
    Data=[]

    for i in range(1,no1+1,1):
        i=int(input())
        Data.append(i)
    print("The List you prepared is:",Data)
    repeat(Data)

def repeat(A):
    no2=int(input("enter the number for which you want check the presence:"))
    count=0
    for i in range(0,len(A),1):
        if no2==A[i]:
            count=count+1
    print("the no of times your number in the list is:",count)
    


if __name__=="__main__":
    main()