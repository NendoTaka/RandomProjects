from Node import TreeNode

class BinaryTree:
    def __init__(self, value):
        self.setRoot(TreeNode(value))
        
    def setRoot(self, node):
        self.root = node
    
    def append(self, value):
        newNode = TreeNode(value)
        self.placeNode(newNode, self.root)
        
    def placeNode(self, newNode, currNode):
        if newNode.value > currNode.value:
            if currNode.right == None:
                currNode.right = newNode
            else:
                self.placeNode(newNode, currNode.right)
        else:
            if currNode.left == None:
                currNode.left = newNode
            else:
                self.placeNode(newNode, currNode.left)
    
    def printTree(self):
        self.printNode(self.root, 0)
    
    def printNode(self, node, depth):
        if node == None:
            return
        
        self.printNode(node.left, depth + 1)
        print((" " * depth) + str(node.value))
        self.printNode(node.right, depth + 1)
