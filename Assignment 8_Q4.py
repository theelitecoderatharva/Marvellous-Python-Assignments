import threading
import pandas as pd


def smallchr(no):
    count=0
    print("the Small chr thread id is:",threading.get_ident())
    for i in no:
        if i.islower():
              count=count+1  
    print("the small character are:",count)


def capchr(no):
    count=0
    print("the Captial thread id is:",threading.get_ident())
    for i in no:
        if i.isupper():
            count=count+1
    print("the Uppercase characters are:",count)


def numb(no):
    count=0
    print("the number thread id is:",threading.get_ident())
    for i in no:
        if i.isdigit():
            count=count+1
    print("the count of numbers are:",count)


def main():
    data=input("enter the string you want to check:")
    print("the main thread id is:",threading.get_ident())

    T1=threading.Thread(target=smallchr,args=(data,))
    T2=threading.Thread(target=capchr,args=(data,))
    T3=threading.Thread(target=numb,args=(data,))

    T1.start()
    T2.start()
    T3.start()
    
    T1.join()
    T2.join()
    T3.join()

if __name__=="__main__":
    main()
    