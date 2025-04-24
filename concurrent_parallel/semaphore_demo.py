import threading
import time

# Semaphore to limit concurrent access to 2 threads
semaphore = threading.Semaphore(2)

def worker(worker_id):
    with semaphore:  # Only 2 threads can acquire the semaphore at a time
        print(f"Worker {worker_id} acquired semaphore")
        time.sleep(2)  # Simulate some work
        print(f"Worker {worker_id} released semaphore")

def main():
    threads = []
    
    # Create 5 threads
    for i in range(5):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
        print(f"Started worker {i}")
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("All workers completed")

if __name__ == "__main__":
    main() 