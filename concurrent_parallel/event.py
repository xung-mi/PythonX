import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for event")
    event.wait()  # Đợi tín hiệu
    print("Event received, continuing")

def trigger():
    time.sleep(1)
    print("Triggering event")
    event.set()  # Gửi tín hiệu

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=trigger)
t1.start()
t2.start()
t1.join()
t2.join()