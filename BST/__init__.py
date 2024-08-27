
class BinaryNode:
    def __init__(self,data:int) -> None:
        self.data = data 
        self.left = None
        self.right = None

#O(log(N)) if the tree is balanced! else it can go to O(N)
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, data: int) -> (BinaryNode | None):
        if not self.root:
            return None
        
        current_node = self.root

        while current_node:
            if data < current_node.data:
                current_node == current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return current_node
            
        return None

    def insert(self, data: int) -> None:
        #first insert becomes the root
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            self.insertNode(data,self.root)
        
    def insertNode(self,data: int, node: BinaryNode) -> None:
        if data < node.data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left = BinaryNode(data)
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right = BinaryNode(data)

    # O(log(N))
    def removeNode(self, data:int, node: BinaryNode | None) -> None:
        if not node:
            return node
        
        #checking child nodes for position
        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)

        # this is the node that we are looking for
        elif data == node.data:

            #check to see if it is a leaf node: has no children
            if not node.left and not node.right:
                #delete node & set to None
                del node
                return None
            
            #only has right child, left is None
            if not node.left:
                tempNode = node.right
                del node
                return tempNode
            #only has right child, left is None
            elif not node.right:
                tempNode = node.left
                del node
                return tempNode
            
            # deleting node with two children
            tempNode = self.getPredecessor(node.left)
            node.data= tempNode.data
            node.left = self.removeNode(tempNode.data, node.left)





    def remove(self, data: int) -> None:
        if self.root:
            self.root.removeNode(data, self.root)
    
    

    # O(log(N))
    # Returning the exact value for the Min
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
    # Finding the position of the min

    def getMin(self, node: BinaryNode) -> int:
        if node.left:
            return self.getMin(node.left)

        return node.data
    
    # O(log(N))
    # Returning the Max Value
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
        
    # Finding the min vale in the tree
    def getMax(self, node:BinaryNode) -> int :
        if node.right:
            return self.getMax(node.right)
        return node.data
    


    def traverseInOrder(self, node: BinaryNode) -> None:

        if node.left:
            self.traverseInOrder(node.left)
        
        print(f"{node.data}")

        if node.right:
            self.traverseInOrder(node.right)

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def getPredecessor(self, node: BinaryNode) -> BinaryNode:
        if node.right:
            return self.getPredecessor(node.right)

        return node

