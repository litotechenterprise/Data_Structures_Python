class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)
        return item

    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)