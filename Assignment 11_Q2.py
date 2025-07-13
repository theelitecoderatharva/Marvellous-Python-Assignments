def rec(A,B):
    if A>B:
        return 1
    #result=A*(A+1)
    #rec(A+1,B)
    return A*rec(A+1,B)
def main():
    no=int(input("enter the number for factorial:"))
    a=1
    ans=rec(a,no)
    print("the factorial is:",ans)
    
if __name__=="__main__":
    main()