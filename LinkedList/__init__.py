

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1


    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


    def empty(self):
        self.head = None
        self.tail = None
        self.length = 0


    def prepend(self,value):
        new_node = Node(value)
        if self.head:
            temp = self.head
            new_node.next = temp 
        else:
            self.tail = new_node
        
        self.head = new_node
        self.length += 1

        return True
            

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        else:
            temp = self.head
            while temp.next.next:
                 temp = temp.next
            last = temp.next
            temp.next = None
            self.tail = temp
            self.length -= 1
            return last
        

    def pop_first(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.tail = None
        
        temp = self.head
        self.head = self.head.next
        self.length -= 1

        return temp
    

    def get(self, index:int):
        if index < 0 or index >= self.length:
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current


    def set_value(self, index,value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp 
            temp = after



