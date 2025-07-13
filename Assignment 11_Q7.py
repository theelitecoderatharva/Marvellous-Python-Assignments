def rec(A,B):
    if A>B:
        return 
    print("*"*A)
    rec(A+1,B)

def main():
    no=int(input("enter the number of stars you want:"))
    a=1
    rec(a,no)

if __name__=="__main__":
    main()