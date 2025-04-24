import threading
import time

# Shared counter
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # Using lock to protect the critical section
            counter += 1

def main():
    threads = []
    
    # Create 5 threads
    for _ in range(5):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print(f"Final counter value: {counter}")  # Should be 500000
    print("Without lock, this value would be less than 500000 due to race conditions")

if __name__ == "__main__":
    main() 