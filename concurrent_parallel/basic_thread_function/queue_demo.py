from queue import Queue
import threading

q = Queue()

def producer():
    for i in range(5):
        q.put(i)
    q.put(None)  # Gửi dấu hiệu kết thúc cho consumer

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
