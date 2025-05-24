def even():
    count=0
    num=1
    while(count<10):
        if(num%2==0):
            print(num,end=" ")
            count=count+1
        num=num+1

if __name__=="__main__":
    even()