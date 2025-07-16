#from threading import Thread
from multiprocessing import Process as Thread  # Monkey-patching
import time

def foo():
    for i in range(10):
        print("foo: counting", i)
        time.sleep(1)

def bar():
    for i in range(10):
        print("bar: counting", i)
        time.sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.start()
    t2.start()

    print("2 processes started, waiting for them to complete.")
    t1.join()
    t2.join()
