def main():
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    A=lambda a,b:a+b

    add=A(num1,num2)
    print("the addition of the numbers you entered is:",add)

if __name__=="__main__":
    main()