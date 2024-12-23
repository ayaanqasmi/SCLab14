import threading

# Shared counter
counter = 0
# Lock for synchronization
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        with lock:  # Synchronize access to the shared counter
            counter += 1

# Create three threads
threads = []
for _ in range(3):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# The final value of counter should be 300
print(f"Final counter value: {counter}")
