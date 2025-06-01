def vowel():
    a=str(input("enter the single charac:"))
    Data=['a','e','i','o','u']

    if len(a)==1 and a.isalpha():
        if a.lower() in Data:
            print("the entered character is vowel")

        else:
            print("the charac is consonant.")
    else:
        print("enter only single charac & that too alphabet only")

if __name__=="__main__":
    vowel()