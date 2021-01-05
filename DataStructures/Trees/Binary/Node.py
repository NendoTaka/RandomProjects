class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def setLeft(self, node):
        self.left = node
        
    def setRight(self, node):
        self.right = node
    
    def setValue(self, value):
        self.value = value