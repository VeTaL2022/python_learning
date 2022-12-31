import threading
import time

# def show(n):
#     for i in range(n):
#         time.sleep(.5)
#         print(i, threading.current_thread().name)
#
#
# thread1 = threading.Thread(target=show, args=(5,), name='th-1')
# thread2 = threading.Thread(target=show, args=(8,), name='th-2')
#
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
#
# for i in range(10):
#     time.sleep(1)
#     print(i)

count = 0

lock = threading.Lock()


# def inc():
#     lock.acquire()
#     global count
#     count += 1
#     print(count)
#     lock.release()
def inc():
    with lock:
        global count
        count += 1
        print(count)


threads = []
for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for item in threads:
    item.join()
