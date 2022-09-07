
# a class for each individual node
class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) 
    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):

        # check to see if list is empty
        if self.head is None:
            return
        
        self.size = self.size -1

        currentNode = self.head
        perviousNode = None

        #Looking for you want to delete
        while currentNode.data != data:
            perviousNode = currentNode
            currentNode = currentNode.nextNode

        # the Node we want to remove is the head
        if perviousNode is None:
            self.head = currentNode.nextNode
        else:
            perviousNode.nextNode = currentNode.nextNode

    # O(1)
    def size1(self):
        return self.size

    # O(N) Not Good
    def size2(self):

        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    # O(N)
    def insertEnd(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        # find last node
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode   

        # set last node to be pointing to newnode
        actualNode.nextNode = newNode

    # traverse is fancy term for printing or looking through the entire list
    def traverseList(self):
        
        actualNode = self.head

        while actualNode is not None:
            print("{d}".format( d = actualNode.data ))
            actualNode = actualNode.nextNode


# Testing Linked List

linkedlist = LinkedList()

linkedlist.insertStart(22)
linkedlist.insertStart(23)
linkedlist.insertStart(44)
linkedlist.insertStart(264)
linkedlist.insertEnd(3435)

print("Items in List")
linkedlist.traverseList()
print("Size of the list")
print(linkedlist.size1())

linkedlist.remove(22)
print("Items in List")
linkedlist.traverseList()
print("New size of the list")
print(linkedlist.size1())