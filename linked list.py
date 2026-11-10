# ASSESSMENT 3.2: LINKED LIST
# Name: James Paul Juat
# Section: BSIT 2-G

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    # Display the linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("NULL")

    # Delete the first node
    def delete(self):
        if self.head is not None:
            removed = self.head.data
            self.head = self.head.next
            return removed

        return None






letters = input("Enter your last name: ").upper()
linked_list = LinkedList()

# Insertion
print("\n--- LINKED LIST INSERTION ---")

for letter in letters:
    linked_list.insert(letter)
    print("Inserted:", letter)
    linked_list.display()

# Deletion
print("\n--- LINKED LIST DELETION ---")

while linked_list.head is not None:
    removed = linked_list.delete()
    print("Deleted:", removed)
    linked_list.display()

print("\nFinal Linked List: EMPTY")


