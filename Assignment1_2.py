def ChkNum():
    print("enter the first number")
    num1=int(input())
    if (num1%2)==0:
        print("even number")
    else:
        print("odd number")


if __name__=="__main__":
    ChkNum()