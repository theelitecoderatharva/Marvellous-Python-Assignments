def main():
    str1=str(input("enter the string:"))
    str2=str()
    for i in range(len(str1)-1,-1,-1):
        str2=str2+str1[i]
    print("new string is:",str2)

    if str1==str2:
        print("the string is palindrome")
    else:
        print("it is not palindrome")
    

if __name__=="__main__":
    main()