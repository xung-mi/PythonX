import threading
import time

def worker(name, duration):
    print(f"Worker {name} started, sleeping for {duration} seconds")
    time.sleep(duration)
    print(f"Worker {name} finished")

# Tạo các luồng
threads = []

# Tạo 2 luồng daemon và 2 luồng non-daemon
for i in range(4):
    is_daemon = i < 2  # 2 luồng đầu là daemon
    t = threading.Thread(target=worker, args=(i, 3), daemon=is_daemon)
    threads.append(t)
    t.start()

# Đợi 2 luồng đầu (daemon) hoàn thành bằng join
print("Main thread: Waiting for first two threads (daemon) to finish")
for i in range(2):
    threads[i].join()

# Kiểm tra trạng thái và tiếp tục
print("Main thread: First two threads finished, continuing")
for i, t in enumerate(threads):
    print(f"Thread {i} is {'still running' if t.is_alive() else 'finished'}")

print("Main thread: Done")