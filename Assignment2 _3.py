def factorial():
    num=int(input("enter the number of which you want the factorial:"))
    sum=1
    if num>0:
        for i in range(1,num+1,1):
            sum=sum*i
        print("the factorial is:",sum)

    else:
        print("the FActorial is 1")        

if __name__=="__main__":
    factorial()