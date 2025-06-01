def large():
    a=int(input("enter the frst number:"))
    b=int(input("enter the second number:"))
    c=int(input("enter the third number:"))
    Data=[a,b,c]
    largest=a
    for i in range(0,len(Data),1):
        if largest<Data[i]:
            largest=Data[i]
    print("the largest among all the numbers is:",largest)


if __name__=="__main__":
    large()