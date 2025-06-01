def evensum():
    Sum=0
    for i in range(1,101,1):
        if i%2==0:
            Sum=Sum+i
    print("The sum of first 100 even nuumber are:",Sum)

if __name__=="__main__":
    evensum()