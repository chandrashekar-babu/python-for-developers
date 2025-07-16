import time

def foo():
    for i in range(10):
        print("foo: counting", i)
        time.sleep(1)

def bar():
    for i in range(10):
        print("bar: counting", i)
        time.sleep(1)

foo()
bar()
