# ASSESSMENT 3.2: STACK
# Name: James Paul Juat
# Section: BSIT 2-G

letters = input("Enter your last name: ").upper()

# Create an empty stack
stack = []

# PUSH operation
print("\n--- STACK PUSH ---")

for letter in letters:
    stack.append(letter)
    print("Pushed:", letter)
    print("Stack:", stack)

# POP operation
print("\n--- STACK POP ---")

while len(stack) > 0:
    removed = stack.pop()
    print("Popped:", removed)
    print("Stack:", stack)

print("\nFinal Stack: EMPTY")