def area(a,b):
    A=float(a*b)
    print("the area is:",A,"sqcm")

def Peri(a,b):
    P=float(2*(a+b))
    print("the perimeter is:",P,"cm")


if __name__=="__main__":
    length=int(input("enter the length:"))
    breadth=int(input("enter the breadth:"))
    area(length,breadth)
    Peri(length,breadth)
    