import threading
import sys

def Evenchk(Even):
    Data=[]
    val1=(Even)
    if val1%2==0:
         for u in range(1,val1+1,1):
             if val1%u==0:
                 Data.append(u)


    print("the evenfact data is:",Data)
    sum=0
    for z in range(0,len(Data),1):
         sum=sum+Data[z]
    print("the sum of even factors is:",sum)

def Oddchk(Odd):
    Data=[]
    val1=(Odd)
    if val1%2!=0:
            for u in range(1,val1+1,1):
                if val1%u==0:
                    Data.append(u)

    print("the oddfact data is:",Data)
    sum=0
    for z in range(0,len(Data),1):
         sum=sum+Data[z]
    print("the sum of odd factors is",sum)

def main():
    a=int(input("r the number of which factor you want:"))


    Evenfactor=threading.Thread(target=Evenchk,args=((a,)))
    OddFactor=threading.Thread(target=Oddchk,args=((a,)))
    Evenfactor.start()
    OddFactor.start()
    Evenfactor.join()
    OddFactor.join()
    print("exit from main")


if __name__=="__main__":
    main()