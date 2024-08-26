

class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

#O(log(N)) if the tree is balanced! else it can go to O(N)
class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        #Checking to see if there is a root Node
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)
     # O(log(N)) if the tree is balanced
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)
    # O(log(N))
    def removeNode(self, data, node):

        if not node:
            return node
        
        # Checking child nodes for position
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        # this is the node were looking for     
        else:

            # checking to see if it is a leaf node: has no children
            if not node.leftChild and not node.rightChild:
                print("Removing Leaf Node......")
                # delete Node & set to None
                del node
                return None


            # Node only has Right child, Left is Null
            if not node.leftChild:
                print("Removing a node with single right child ")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode

            
            print("Deleting node with two children")
            tempNode = self.getPedeccor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node



    # O(log(N))
    # Returning the exact value for the Min
    def getMinValue(self):
        if self.root:
            return self.root.getMin(self.root)
    # Finding the position of the min
    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)

        return node.data


    # O(log(N))
    # Returning the Max Value
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    # Finding the Position of the Min Value
    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def travserse(self):
        if self.root:
            self.travserseInOrder(self.root)

    # O(N)
    def travserseInOrder(self, node):

        if node.leftChild:
            self.travserseInOrder(node.leftChild)
        
        print("{a}".format(a=node.data))

        if node.rightChild:
            self.travserseInOrder(node.rightChild)



