
A= lambda b: b**2 

def main():
    print("enter the number for which the square is required:")
    c=float(input())
    c=A(c)
    print(c)

if __name__=="__main__":
    main()