A= lambda a,b: a*b

def main():
    print("enter the first number:")
    c=float(input())
    print("enter the second number:")
    d=float(input())
    c=A(c,d)
    print(c)

if __name__=="__main__":
    main()