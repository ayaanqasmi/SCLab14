import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_squares():
    for i in range(1, 11):
        print(i ** 2)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_squares)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
