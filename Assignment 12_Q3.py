class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self):
        self.value1=float(input("enter the first number"))
        self.value2=float(input("enter the second number"))

    def Addition(self):
        result=self.value1+self.value2
        return result
    
    def Mutliplication(self):
        result=self.value1*self.value2
        return result
    
    def Subtraction(self):
        result=self.value1-self.value2
        return result
    
    def Division(self):
        result=self.value1/self.value2
        return result

def main():
    obj1=Arithmetic()
    obj1.accept()

    ret1=obj1.Addition()
    print("the addition is:",ret1)
    ret2=obj1.Subtraction()
    print("the subtraction is:",ret2)
    ret3=obj1.Mutliplication()
    print("the multiplication is:",ret3)
    ret4=obj1.Division()
    print("the division is:",ret4)

if __name__=="__main__":
    main()