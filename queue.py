# ASSESSMENT 3.2: QUEUE
# Name: James Paul Juat
# Section: BSIT 2-G

from collections import deque

letters = input("Enter your last name: ").upper()

# Create an empty queue
queue = deque()

# ENQUEUE operation
print("\n--- QUEUE ENQUEUE ---")

for letter in letters:
    queue.append(letter)
    print("Enqueued:", letter)
    print("Queue:", list(queue))

# DEQUEUE operation
print("\n--- QUEUE DEQUEUE ---")

while len(queue) > 0:
    removed = queue.popleft()
    print("Dequeued:", removed)
    print("Queue:", list(queue))

print("\nFinal Queue: EMPTY")
