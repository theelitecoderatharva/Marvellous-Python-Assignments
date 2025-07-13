def rec(A,B,ntime):
    if ntime>B:
        return 1
    return A*rec(A,B,ntime+1)

def main():
    no=int(input("enter the power:"))
    a=int(input("enter the base:"))
    powertime=1
    ans=rec(a,no,powertime)
    print("the power func is:",ans)

if __name__=="__main__":
    main()