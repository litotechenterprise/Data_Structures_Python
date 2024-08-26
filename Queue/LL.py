class Node:

    def __init__(self, data):
        self.data = data
        self.pre = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def peek(self):
        return

    def enqueue(self, data):
        new_last_node = Node(data)
        is_empty_list = not self.first and not self.last

        if is_empty_list:
            self.first = new_last_node
            self.last = new_last_node
        else:
            self.last.prev = new_last_node
            self.last = new_last_node

        return new_last_node
    

    def dequeue(self):
        removed_item = self.first

        if not removed_item:
            return None
        
        if self.first == self.last:
            self.last = None

        self.first =removed_item.prev

        return removed_item



    def dequeue(self):
        pass

