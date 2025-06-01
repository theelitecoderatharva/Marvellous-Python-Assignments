def starpattern():
    no1=int(input("enter the number of line you want star pattern:"))
    for i in range(1,no1+1,1):
        u=1
        while(u<=i):
            print("*", end=" ")
            u=u+1
        print()
        

if __name__=="__main__":
    starpattern()