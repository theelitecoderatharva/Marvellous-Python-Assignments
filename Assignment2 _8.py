def num():
    no1=int(input("enter the number you want"))
    for i in range(1,no1+1,1):
        j=1
        while(j<=i):
            print(j,end=" ")
            j=j+1
        print()

if __name__=="__main__":
    num()