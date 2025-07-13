import time
import schedule
import threading

def thread1():


def thread2():


def thread3():

def main():
    no=5
    t1=threading.Thread(target=thread1,args=(no,))
    t2=threading.Thread(target=thread2,args=(no,))
    t3=threading.Thread(target=thread3,args=(no,))

   
    t1.start()
    t1.join()

if __name__=="__main__":
    main()