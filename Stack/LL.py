class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None

    
class Stack:
    def __init__(self):
        self.last = None

    def peek(self):
        return self.last

    def push(self, item):
        prev_last = self.last

        self.last = Node(item)
        self.last.prev = prev_last

        return self.last

    def pop(self):
        removed_item = self.last
        # Update `last` as long as we have items left in the stack
        if removed_item:
            self.last = removed_item.prev

        return removed_item


