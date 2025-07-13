def rec(A,B,ntime):
    if B>=ntime:
        return 0
    if A[B]=='0':
        return 1+rec(A,B+1,ntime)
    return rec(A,B+1,ntime)

def main():
    no=int(input("enter the number:"))
    a=str(no)
    strlen=len(a)
    no1=0
    ans=rec(a,no1,strlen)
    print("the number of zeroes are:",ans)

if __name__=="__main__":
    main()