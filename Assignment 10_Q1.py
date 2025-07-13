def main():
    num=float(input("enter the number:"))

    A=lambda a:a**2

    square=A(num)
    print("the square of the number you entered is:",square)

if __name__=="__main__":
    main()