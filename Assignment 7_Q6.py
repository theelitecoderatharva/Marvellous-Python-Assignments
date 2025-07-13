import sys
def primechk(a):
    if a>1:
        if a%2!=0 or a==2:
            return True
        elif a%3!=0 or a==3:
            return True
        
    else:
        return False

def main():
    a=int(sys.argv[1])
    Data=[]
    for i in range(2,a+2,1):
        Data.append(int(sys.argv[i]))
    print(Data)

    filt1=list(filter(primechk,Data))
    print("The filtered data is:",filt1)


if __name__=="__main__":
    main()