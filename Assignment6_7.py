import sys
def Listprep():    
    Data=[]
    a=int(sys.argv[1])
    
    for i in range(2,a+2,1):
        Data.append(sys.argv[i])
    print("the data you entered is:",Data)
    largest(Data)

def largest(A):
    Great=A[0]
    for i in range(0,len(A),1):
        if Great<A[i]:
            Great=A[i]
    print("the greatest number is:",Great)

Listprep()