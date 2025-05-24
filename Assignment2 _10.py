def numadd():
    num=int(input("enter the number"))
    a=str(num)
    add=0
    for i in range(0,len(a),1):
        add=add+int(a[i])
    print("the sum is:",add)

if __name__=="__main__":
    numadd()