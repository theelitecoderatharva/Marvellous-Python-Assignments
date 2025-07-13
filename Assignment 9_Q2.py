import multiprocessing

def square(num):
    return num*num

def main():
    no1=[1,2,3,4,5,6]
    pool = multiprocessing.Pool()
    result = pool.map(square, no1)
    pool.close()
    pool.join()
    print("the dataset of numbers are:",no1)
    print("the dataset of numbers are:",result)

if __name__=="__main__":
    main()