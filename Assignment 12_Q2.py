class circle:
    PI=3.1452
    
    def __init__(self):
        self.radius=0
        self.area=0
        self.circumference=0

    def Accept(self):
        self.radius=float(input("enter the radius:"))

    def CalculateArea(self):
        self.area=circle.PI*(self.radius**2)

    def CalculateCircumference(self):
        self.circumference=2*circle.PI*(self.radius)

    def Display(self):
        print("the radius entered is:",self.radius)
        print("the area calculated is:",self.area)
        print("the circumference calculated is",self.circumference)
    

def main():
    circle1=circle()
    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    circle1.Display()



if __name__=="__main__":
    main()