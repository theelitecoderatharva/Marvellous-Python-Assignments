from MarvellousNum import ChkPrime as B

def main():
    no1=int(input("enter the number of items you wnat"))
    Data=[]

    for i in range(1,no1+1,1):
        i=int(input())
        Data.append(i)
    print("The List you prepared is:",Data)
    sum=0
    for i in range(len(Data)):
         if B(Data[i]):
             sum=sum+Data[i]
       
    print("the sum of prime numbers is:",sum)

if __name__=="__main__":
    main()

