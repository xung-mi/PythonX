import threading
import time

def worker(worker_id, sleep_time):
    print(f"Worker {worker_id} started")
    time.sleep(sleep_time)
    print(f"Worker {worker_id} completed")

def main():
    threads = []
    
    # Create threads with different sleep times
    sleep_times = [1, 2, 3, 4, 5]
    for i, sleep_time in enumerate(sleep_times):
        thread = threading.Thread(target=worker, args=(i, sleep_time))
        threads.append(thread)
        thread.start()
        print(f"Started thread {i} with sleep time {sleep_time}")
    
    # Check thread status using isAlive
    while any(thread.is_alive() for thread in threads):
        print("\nChecking thread status:")
        for i, thread in enumerate(threads):
            status = "alive" if thread.is_alive() else "completed"
            print(f"Thread {i} is {status}")
        time.sleep(1)
    
    # Using join to wait for all threads
    print("\nWaiting for all threads to complete...")
    for thread in threads:
        thread.join()
    
    print("\nAll threads have completed")

if __name__ == "__main__":
    main() 