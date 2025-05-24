def num():
    no1=int(input("enter the number you want"))
    sum=0
    for i in range(1,no1+1,1):
        j=1
        while(j<=no1):
            print(j,end=" ")
            j=j+1
        print()

if __name__=="__main__":
    num()