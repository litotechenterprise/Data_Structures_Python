class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return 
        
        self.head.value, self.tail.value = self.tail.value, self.head.value


    def reverse(self):
        if self.length <= 1:
            return 
        
        current = self.head
        while current is not None:
            temp_next = current.next
            current.next = current.prev
            current.prev = temp_next
            current = temp_next

        self.head, self.tail = self.tail, self.head