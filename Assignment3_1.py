import sys

def addition(A):
    i=0
    sum=0
    while(i<len(A)):
        sum=sum+A[i]
        i=i+1
   
    print("the sum is:",sum)

def main():
    a=int(sys.argv[1])
    Data=[]
    for i in range(2,2+a,1):
        Data.append(int(sys.argv[i]))
    #return Data
    print(Data)
    addition(Data)
if __name__=="__main__":
    main()