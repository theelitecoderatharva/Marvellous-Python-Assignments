import threading

def order(num):
    for i in range(1,num+1,1):
        print(i)

def reverseorder(num):
    for i in range(num,0,-1):
        print(i)

def main():
    border="-"*25
    no=50
    Thread1=threading.Thread(target=order,args=(no,))
    Thread2=threading.Thread(target=reverseorder,args=(no,))
    Thread1.start()
    Thread1.join()
    print(border)
    Thread2.start()
    Thread2.join()

if __name__=="__main__":
    main()