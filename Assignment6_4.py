def fact():
    no1=int(input("enter the number for factorial:"))
    Mult=1
    for i in range(1,no1+1,1):
        Mult=Mult*i
    print("the factorial is:",Mult)

if __name__=="__main__":
    fact()