def rec(A,B):
    if A>B:
        return 0
    return A+rec(A+1,B)

def main():
    no=int(input("enter the number:"))
    a=1
    ans=rec(a,no)
    print("the sum is:",ans)

if __name__=="__main__":
    main()