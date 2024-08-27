
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
            self.__insertNode(data,self.root)
        
    def __insertNode(self,data: int, node: BinaryNode) -> None:
        if data < node.data:
            if node.left:
                self.__insertNode(data,node.left)
            else:
                node.left = BinaryNode(data)
        else:
            if node.right:
                self.__insertNode(data,node.right)
            else:
                node.right = BinaryNode(data)



    def recursive_insert(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        return self.__r_insert(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return BinaryNode(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    # O(log(N))
    def __removeNode(self, data:int, node: BinaryNode | None) -> None:
        if not node:
            return node
        
        #checking child nodes for position
        if data < node.data:
            node.left = self.__removeNode(data, node.left)
        elif data > node.data:
            node.right = self.__removeNode(data, node.right)

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
            tempNode = self.__getPredecessor(node.left)
            node.data= tempNode.data
            node.left = self.__removeNode(tempNode.data, node.left)


    def remove(self, data: int) -> None:
        if self.root:
            self.__removeNode(data, self.root)
    

    # O(log(N))
    # Returning the exact value for the Min
    def getMinValue(self):
        if self.root:
            return self.__getMin(self.root)
    # Finding the position of the min

    def __getMin(self, node: BinaryNode) -> int:
        if node.left:
            return self.__getMin(node.left)

        return node.data
    
    # O(log(N))
    # Returning the Max Value
    def getMaxValue(self):
        if self.root:
            return self.__getMax(self.root)
        
    # Finding the min vale in the tree
    def __getMax(self, node:BinaryNode) -> int :
        if node.right:
            return self.__getMax(node.right)
        return node.data
    
    # def __traverseInOrder(self, node: BinaryNode) -> None:
    #     if node.left:
    #         self.__traverseInOrder(node.left)
    #     print(f"{node.data}")

    #     if node.right:
    #         self.__traverseInOrder(node.right)

    # def traverse(self):
    #     if self.root:
    #         self.__traverseInOrder(self.root)

    def __getPredecessor(self, node: BinaryNode) -> BinaryNode:
        if node.right:
            return self.__getPredecessor(node.right)

        return node

    def BFS(self):
        if self.root is None:
            return None
        results = []
        queue = [self.root]
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        return results
    
    def DFS_Post_Order(self):
        if self.root is None:
            return None
        results = []
        def traverse(current_node: BinaryNode):
            if current_node.left is not None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right)

            results.append(current_node.data)

        traverse(self.root)
        return results
    
    def DFS_In_Order(self):
        if self.root is None:
            return None
        results = []
        def traverse(current_node:BinaryNode):
            if current_node.left is not None:
                traverse(current_node.left)

            results.append(current_node.data)

            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return results