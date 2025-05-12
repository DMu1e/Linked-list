class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):  
        if index < 0:
            print("Index must be a positive number")
            return

        if index == 0:
            self.insert_at_start(data)  
            return

        new_node = Node(data)
        current = self.head
        position = 0

        while current and position < index - 1:
            current = current.next
            position += 1

        if not current:
            print(f"Index {index} out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index < 0:
            print("Index cannot be negative")
            return

        if self.isempty():
            print("The list is empty, please insert elements")
            return

        if index == 0:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted node at index 0 with value {deleted_value}")
            return

        current = self.head
        position = 0
        while current and position < index - 1:
            current = current.next
            position += 1

        if not current or not current.next:
            print(f"Index {index} is out of bounds")
            return

        deleted_value = current.next.data
        current.next = current.next.next
        print(f"Deleted node at index {index} with value {deleted_value}")

    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                return position  
            current = current.next
            position += 1

        return -1 

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")

ll = LinkedList()
ll.insert_at_start(7)
ll.insert_at_end(12)
ll.insert_at_index(1, 5)
ll.display()                 
print(ll.search(7))         
ll.delete_at_index(1)
ll.display()                
