from threading import Thread
import time

def foo():
    for i in range(1_000_000):
        print("foo: counting", i)
       

def bar():
    for i in range(1_000_000):
        print("bar: counting", i)
     
t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()
# ----
print("2 threads started, waiting for them to complete.")

t1.join()
print("Thread 1 completed.")

t2.join()
print("Thread 2 completed.")