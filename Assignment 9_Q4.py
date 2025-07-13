import multiprocessing
import threading
import time

def addmlp(num):
    sum=0
    while(num>0):
        sum=sum+num
        num=num-1
    print("the sum of numbers by multiprocessing are:",sum)

def addt(num):
    sum=0
    while(num>0):
        sum=sum+num
        num=num-1
    print("the sum of numbers by threading are:",sum)


def main():
    no1=10000000
    poolstarttime=time.time()
    p1 = multiprocessing.Process(target=addmlp,args=(no1,))
    p1.start()
    p1.join()
    poolendtime=time.time()
    
    print("the exec time of multiprocessing is:",(poolendtime-poolstarttime))

    threadstarttime=time.time()
    T1=threading.Thread(target=addt,args=(no1,))
    T1.start()
    T1.join()
    threadendime=time.time()
    print("the thread exec time is:",(threadendime-threadstarttime))

if __name__=="__main__":
    main()