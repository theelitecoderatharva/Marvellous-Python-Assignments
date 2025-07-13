def rec(b,a):
    if b>a:
        return
    print(b,end=' ')
    rec(b+1,a)

def main():
    no=int(input("please enter the number"))
    rec(1,no)

if __name__=="__main__":
    main()