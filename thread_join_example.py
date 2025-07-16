from threading import Thread, current_thread
import time

def counting_loop(count, delay):
    t = current_thread()
    print(f"counting_loop() is run by {t}")

    for i in range(count):
        print(f"{t.name} counting", i)
        time.sleep(delay)
    print(f"{t.name}: completed.")
     
t1 = Thread(target=counting_loop, args=(5, 2))
t2 = Thread(target=counting_loop, kwargs={"count": 10, "delay": 1})

print("Created 2 threads:")
print(f"{t1=}\n{t2=}")

t1.start()
t2.start()
# ----
print("2 threads started")

counting_loop(4, 1)
print(f"main: waiting for 2 threads to complete")

t1.join()
print("Thread 1 completed.")

t2.join()
print("Thread 2 completed.")