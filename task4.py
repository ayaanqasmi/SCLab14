import threading
import random

# Bank account class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, balance: {self.balance}")
            else:
                print("Insufficient funds")

# Bank account instance
account = BankAccount()

def perform_transaction():
    for _ in range(10):
        if random.choice([True, False]):
            amount = random.randint(10, 50)
            account.deposit(amount)
        else:
            amount = random.randint(10, 50)
            account.withdraw(amount)

# Create multiple threads (clients)
threads = []
for _ in range(5):
    thread = threading.Thread(target=perform_transaction)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final balance: {account.balance}")
