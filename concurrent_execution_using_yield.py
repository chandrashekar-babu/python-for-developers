import time

def foo():
    for i in range(10):
        print("foo: counting", i)
        yield
        time.sleep(1)

def bar():
    for i in range(10):
        print("bar: counting", i)
        yield
        time.sleep(1)

g1 = foo()
g2 = bar()

for _, _ in zip(g1, g2):
    pass
