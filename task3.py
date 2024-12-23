import threading
from collections import deque

# Shared data structure (using deque for demonstration)
shared_list = deque()

# Lock to ensure thread safety
lock = threading.Lock()

def modify_list():
    for i in range(5):
        with lock:
            shared_list.append(i)
            print(f"Added {i} to the shared list")

# Create multiple threads
threads = []
for _ in range(5):
    thread = threading.Thread(target=modify_list)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final shared list: {list(shared_list)}")
