def prime():
    num=int(input("enter the number:"))
    if num==1:
        print("the number is neither prime nor composite")
    elif num%2==0:
        print("the number is composite")
    else:
        print("the number is prime")    

if __name__=="__main__":
    prime()    