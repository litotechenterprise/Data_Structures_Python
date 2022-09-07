class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.RightChild = None
        self.LeftChild = None

class AVL(object):

    def __init__(self):
        self.root = None


    def traverse(self):

        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):

        if node.LeftChild:
            self.traverseInOrder(node.LeftChild)

        print("{a}".format(a=node.data))

        if node.RightChild:
            self.traverseInOrder(node.RightChild)

        
        

    def insert(self, data):
        self.root = self.insertNode(data, self.root)


    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.LeftChild = self.insertNode(data, node.LeftChild)
        else:
            node.RightChild = self.insertNode(data, node.RightChild)
        
        node.height = max(self.calcHeight(node.LeftChild), self.calcHeight(node.RightChild)) + 1

        return self.settleViolation(data, node)


    def settleViolation(self, data, node):

        balance = self.calcBalance(node)

        # case 1 -> left left heavy situation
        if balance > 1 and data < node.LeftChild.data:
            print("Left Left heavy situation")
            return self.rotateRight(node)

        # case 2 -> right right heavy situation --> single left rotation
        if balance < -1 and data > node.RightChild.data:
            print("right right heavy situation")
            return self.rotateLeft(node)

        # case 3 -> Left Right Heavy situation 
        if balance > 1 and data > node.LeftChild.data:
            print('Left Right Heavy Situation')
            node.LeftChild = self.rotateLeft(node.LeftChild)
            return self.rotateRight(node)

        # case 4 -> Right Left Heavy situation
        if balance < -1 and data < node.RightChild.data:
            print('Right Left Heavy Situation')
            node.RightChild = self.rotateRight(node.RightChild)
            return self.rotateLeft(node)

        return node


    

    def calcHeight(self, node):

        if not node:
            return -1

        return node.height

    # if it returns value > 1 it means it is a left heavy tree --> right rotation
    # ........            < -1 it means it is a right heavy tree --> left rotation
    def calcBalance(self, node):
        
        if not node:
            return 0

        return self.calcHeight(node.LeftChild) - self.calcHeight(node.RightChild)


    def rotateRight(self, node):
        print("Rotating Right on node {a}".format(a=node.data))

        tempLeftChild = node.LeftChild
        t = tempLeftChild.RightChild

        tempLeftChild.RightChild = node
        node.LeftChild = t

        node.height = max(self.calcHeight(node.LeftChild), self.calcHeight(node.RightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.LeftChild), self.calcHeight(tempLeftChild.RightChild)) + 1

        return tempLeftChild




    def rotateLeft(self, node):
        print("Rotating Left on node {a}".format(a = node.data))

        tempRightChild = node.RightChild
        t = tempRightChild.LeftChild

        tempRightChild.LeftChild = node
        node.RightChild = t

        node.height = max(self.calcHeight(node.LeftChild), self.calcHeight(node.RightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.LeftChild), self.calcHeight(tempRightChild.RightChild)) + 1

        return tempRightChild



    def remove(self, data):
        
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.LeftChild = self.removeNode(data, node.LeftChild)

        elif data > node.data:
            node.RightChild = self.removeNode(data, node.RightChild)

        else:

            if not node.LeftChild and not node.RightChild:
                print('Removing a leaf node')
                del node
                return None

            if not node.LeftChild:
                print('Removing node with right child')
                tempNode = node.RightChild
                del node
                return tempNode

            elif not node.RightChild:
                print('Removing node with left child')
                tempNode = node.LeftChild
                del node
                return tempNode

            print('Removing Node with two children')
            tempNode = self.getPredecessor(node.LeftChild)
            node.data = tempNode.data
            node.LeftChild = self.removeNode(tempNode.data, node.LeftChild)

        # if a tree has a single node
        if not node:
            return node             

        node.height = max(self.calcHeight(node.LeftChild), self.calcHeight(node.RightChild)) + 1

        balance = self.calcBalance(node)

        # left left case
        if balance > 1 and self.calcBalance(node.LeftChild) >= 0:
            return self.rotateRight(node)

        # left right case
        if balance > 1 and self.calcBalance(node.LeftChild) < 0:
            node.LeftChild = self.rotateLeft(node.LeftChild)
            return self.rotateRight(node)

        # right right case
        if balance < -1 and self.calcBalance(node.RightChild) <= 0:
            return self.rotateLeft(node)

        # right left case
        if balance < -1 and self.calcBalance(node.RightChild) > 0:
            node.RightChild = self.rotateRight(node.RightChild)
            return self.rotateLeft(node)


        return node
          

    def getPredecessor(self, node):

        if node.RightChild:
            return self.getPredecessor(node.RightChild)

        return node



# Testing

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)

print('Before removal')

avl.traverse()



avl.remove(5)
avl.remove(4)

print('After Removal')
avl.traverse()