def primechk():
    no1=int(input("enter the number for primecheck:"))
    count=0
    for i in range(1,no1+1,1):
        if no1%i==0:
            count=count+1
    if no1==1:
        print("the number is neither prime nor composite")
    elif count==2:
        print("the number is prime")
    else:
        print("the number is composite")

if __name__=="__main__":
    primechk()