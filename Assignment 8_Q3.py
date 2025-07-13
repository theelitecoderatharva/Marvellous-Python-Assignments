import threading

def evenchk(no):
    evenlist=[]
    for i in no:
        if i%2==0:
            evenlist.append(i)
    return evenlist

def oddchk(no):
    oddlist=[]
    for i in no:
        if i%2!=0:
            oddlist.append(i)
    return oddlist


def evensum(no):
    sum=0
    for i in no:
        sum=sum+i
    print("the even sum is:",sum)


def oddsum(no):
    sum=0
    for i in no:
        sum=sum+i
    print("the odd sum is:",sum)


def main():
    no1=int(input("enter the no of inputs you want to provide"))
    datalist=[]
    for i in range(0,no1,1):
        numb=int(input())
        datalist.append(numb)


    print("the list entered is:",datalist)

    evenlist=evenchk(datalist)
    oddlist=oddchk(datalist)

    T1=threading.Thread(target=evensum,args=(evenlist,))
    T2=threading.Thread(target=oddsum,args=(oddlist,))

    T1.start()
    T2.start()
  

    T1.join()
    T2.join()
   
if __name__=="__main__":
    main()
    