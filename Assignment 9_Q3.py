import multiprocessing

def fact(num):
    factnum=1
    while num > 0 :
        #print((num))
        factnum=factnum*((num))
        num=(num)-1
        #print((num))
    return factnum
    
def main():
    no1=[1,2,3,4,5,6]
    pool = multiprocessing.Pool()
    result = pool.map(fact,no1)
    pool.close()
    pool.join()
    print("the dataset of numbers are:",no1)
    print("the dataset of numbers are:",result)
    fact((no1))

if __name__=="__main__":
    main()