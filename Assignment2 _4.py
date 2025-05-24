def factor():
    fact=int(input("enterr the number your want the factor of:"))
    sum=[]
    for i in range(1,fact+1,1):
        if fact%i==0:
            sum.append(i)
    print("the list of the numbers which are factors of the number is:", sum)
    add=0
    for i in range(0,len(sum),1):
        add=add+sum[i]
    print("the addition of factors is:",add)    


if __name__=="__main__":
    factor()