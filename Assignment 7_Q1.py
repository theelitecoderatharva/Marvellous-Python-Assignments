def main():
    a=float(input("enter the number:"))
    A=lambda b:b**2
    C=lambda c:c**3
    print("the square is:",A(a))
    print("the cube is:",C(a))

if __name__=="__main__":
    main()