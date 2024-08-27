
class Node():
    def __init__(self, data: int):
        self.data = data
        self.height = 0
        self.right: Node| None = None
        self.left: Node| None = None


class AVL:
    def __init__(self):
        self.root = None

    def traverseInOrder(self,node:Node):
        if node.left:
            self.traverseInOrder(node.left)

        print(f"{node.data}")

        if node.right:
            self.traverseInOrder(node.right)

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def calcHeight(self, node:Node|None) -> int:
        if not node:
            return -1

        return node.height
    
    # if it returns value > 1 it means it is a left heavy tree --> right rotation
    # < -1 it means it is a right heavy tree --> left rotation
    def calcBalance(self, node:Node | None):
        if not node:
            return 0

        return self.calcHeight(node.left) - self.calcHeight(node.right)
    

    def rotateRight(self, node:Node) -> Node:
        print(f"Rotating right on node {node.data}")

        tempLeft = node.left
        t = tempLeft.right

        tempLeft.right = node
        node.left = t

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempLeft.height = max(self.calcHeight(tempLeft.left), self.calcHeight(tempLeft.right)) + 1
        return tempLeft
    

    def rotateLeft(self, node:Node) -> Node:
        print(f"Rotating left on node{node.data}")

        tempRight = node.right
        t = tempRight.left

        tempRight.left = node
        node.right = t

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempRight.height = max(self.calcHeight(tempRight.left), self.calcHeight(tempRight.right)) + 1

        return tempRight


    def insertNode(self,data:int,node:Node|None) -> Node:
        if not node:
            return Node(data)
        
        if data < node.data:
            node.left = self.insertNode(data,node.left)
        else:
            node.right = self.insertNode(data,node.right)

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.RightChild)) +1

        return self.settleViolation(data, node)

    def insert(self, data:int):
        self.root = self.insertNode(data, self.root)
    

    
    def settleViolation(self, data:int, node: Node) -> Node: 
        balance = self.calcBalance(node)
        #case 1 -> left left heavy
        if balance > 1 and data < node.left.data:
            print("left left heavy situation")
            return self.rotateRight(node)
        
        #case 2 -> right right heavy -> single left rotation
        if balance < -1 and data > node.left.data:
            print("right right heavy situation")

        #case 3 -> left right heavy situation
        if balance > 1 and data > node.left.data:
            print("left right heavy situation")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        
        #case 4 -> Return Left Heavy situation
        if balance < -1 and data < node.right.data:
            print('right left heavy situation')
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        
        return node

    def getPredecessor(self, node: Node) -> Node:
        if node.right:
            return self.getPredecessor(node.right)

        return node
    

    def remove(self, data: int):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data:int, node:Node|None) -> None:
        if not node:
            return node
        
        if data < node.data:
            node.left = self.removeNode(data, node.left)

        elif data > node.data:
            node.right = self.removeNode(data, node.right)

        else:
            if not node.left and not node.right:
                # removing left node
                del node
                return None
            
            # only right child, left is none
            if not node.left:
                tempNode = node.right
                del node 
                return tempNode
            # only left child, right is none
            elif not node.right:
                tempNode = node.left
                del node
                return tempNode
            
            tempNode = self.getPredecessor(node.left)
            node.data = tempNode.data
            node.left = self.removeNode(tempNode.data, node.left)


            node.height = max(self.calcHeight(node.LeftChild), self.calcHeight(node.RightChild)) + 1
            
            return self.settleViolation(data, node)