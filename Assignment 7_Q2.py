import sys
def main():
    a=int(sys.argv[1])
    Data=[]
    for i in range(2,a+2,1):
        Data.append(int(sys.argv[i]))
    print("the data is:",Data)

    Add= lambda a:a*2
    newlist=list(map(Add,Data))
    print("the new list is:",newlist)

if __name__=="__main__":
    main()