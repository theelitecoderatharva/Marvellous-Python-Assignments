def star():
    num=int(input("enter the number of line stars you want"))
    
    for i in range(num,0,-1):
         j=1
         while(j<=i):
              print("*",end=" ")
              j=j+1
         print()     

if __name__=="__main__":
    star()
