def ChkPrime(A):
    sum=0
    if A>2:
        for i in range(2,A,1):
            if A%2==0:
                break
            elif A%3==0:
                break
            else:
                return True
                

if __name__=="__main__":
    ChkPrime()
