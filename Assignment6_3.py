def table():
    no1=int(input("enter the number of which table you want:"))
    for i in range(1,11,1):
        print(no1,"*",i,"=",(no1*i))


if __name__=="__main__":
    table()