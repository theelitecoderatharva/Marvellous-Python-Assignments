def vote():
    age=int(input("enter your age:"))
    if age>=18:
        print("eligible to vote")
    else: 
        print("not eligible to vote")

if __name__=="__main__":
    vote()