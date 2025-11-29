import threading

def nums(num):
    for i in range(1,num+1):
        print(i)
def squrs(num):
    for i in range(1,num+1):
        print(i*i)
t1=threading.Thread(target=nums,args=(10,))
t2=threading.Thread(target=squrs,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
from multiprocessing import Process

def fact(num):
    if num<=0:
        return 1
    else:
        return num*fact(num-1)
def fact_worker(num):
    print(f"Factorial of {num} is {fact(num)}")
nums=[5, 10, 15, 20]
pro=[]
for num in nums:
    t1=Process(target=fact_worker,args=(num,))
    pro.append(t1)
    t1.start()
for num in pro:
    num.join()
