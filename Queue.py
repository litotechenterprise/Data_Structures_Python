class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)
        

# Testing Queue

queue = Queue()
queue.enqueue(30)
queue.enqueue(45)
queue.enqueue(6654)
queue.enqueue(23)
queue.enqueue(345)

print("Queue Size: ", queue.sizeQueue())
print("dequeue: ", queue.dequeue())
print("dequeue: ", queue.dequeue())
print("dequeue: ", queue.dequeue())
print("Queue Size: ", queue.sizeQueue())
print("Peek of Queue: ", queue.peek())

