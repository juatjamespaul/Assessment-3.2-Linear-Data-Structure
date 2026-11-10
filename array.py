# ASSESSMENT 3.2: ARRAY
# Name: James Paul Juat
# Section: BSIT 2-G

letters = input("Enter your last name: ").upper()

# Create an empty array
array = []

# Insertion
print("\n--- ARRAY INSERTION ---")

for letter in letters:
    array.append(letter)
    print("Inserted:", letter)
    print("Array:", array)

# Deletion
print("\n--- ARRAY DELETION ---")

while len(array) > 0:
    removed = array.pop(0)
    print("Removed:", removed)
    print("Array:", array)

print("\nFinal Array: EMPTY")