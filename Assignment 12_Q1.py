class Demo:
    def __init__(self,A,B):
        print("inside constructor")
        self.no1=A
        self.no2=B

    def __del__(self):
        print("inside destructor")

    def fun(self):
        Addition=self.no1+self.no2
        return Addition

    def gun(self):
        Subtraction=self.no1-self.no2
        return Subtraction


def main():
    no1=int(input("enter the first number"))
    no2=int(input("enter the second number"))
    no3=int(input("enter the third number"))
    no4=int(input("enter the fourth number"))

    obj1=Demo(no1,no2)
    obj2=Demo(no3,no4)

    ret=obj1.fun()
    print(ret)
    ret=obj2.fun()
    print(ret)
    ret=obj1.gun()
    print(ret)
    ret=obj2.gun()
    print(ret)


if __name__=="__main__":
    main()