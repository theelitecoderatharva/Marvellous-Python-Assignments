import threading

def Dispeven(Even):
    EvenData=[]
    for i in range (0,len(Even),1):

        if int(Even[i])%2==0:
            EvenData.append(Even[i])
    print("the even numbers are:",EvenData)


def Dispodd(Odd):
    OddData=[]
    for i in range (0,len(Odd),1):

        if int(Odd[i])%2!=0:
            OddData.append(Odd[i])
    print("the odd numbers are:",OddData)

def main():
    print("the thread id id is:",threading.get_ident())
    Data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    T1=threading.Thread(target=Dispeven,args=((Data),))
    T2=threading.Thread(target=Dispodd,args=((Data),))
    #print("the even numbers are:",T1)
    #print("the odd numbers are:",T2)
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__=="__main__":
    main()