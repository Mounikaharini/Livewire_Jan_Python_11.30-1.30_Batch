
#single thread

""" task1 will excute first then only task 2 excute after 2 seconds """
import time

def task1():
    print("hi")

def task2():
    print("hello")

task1()
time.sleep(2)
task2()


#multi-thread

import threading
import time
def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")
t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))
t1.start()
t2.start()
t1.join()
t2.join()

import threading
import time
def task1():
    for i in range(5):
        time.sleep(1)
        print("hi")
def task2():
    for i in range(5):
        time.sleep(2)
        print("hello")
t1 = threading.Thread(target=task1,daemon=True)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()


