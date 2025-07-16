from threading import Thread
import time

def foo():
    for i in range(10):
        print("foo: counting", i)
        time.sleep(1)

def bar():
    for i in range(10):
        print("bar: counting", i)
        time.sleep(1)

t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

print("2 threads started, waiting for them to complete.")
t1.join()
t2.join()
