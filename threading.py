import time 
import threading
def cube(num):
    for n in num:
        print("cube:",n*n,"\n")
        time.sleep(0.2)
def circle(num):
    for n in num:
        print("circle:",n+n,"\n")
        time.sleep(0.1)
arr = [4,6,7,8,9]
t1=threading.Thread(target=cube,args=(arr,))
t2=threading.Thread(target=circle,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()






