from Node import LinkedNode

class DoublyLinkedList:
    def __init__(self, value):
        self.setRoot(LinkedNode(value, None))
        
    def setRoot(self, node):
        self.root = node
    
    def append(self, value):
        lastNode = self.getLastNode()
        lastNode.next = LinkedNode(value, lastNode)
        
    def getLastNode(self):
        currNode = self.root
        while currNode.next != None:
            currNode = currNode.next
        
        return currNode
    
    def printList(self):
        currNode = self.root
        print("[", end="")
        while currNode.next != None:
            print(str(currNode.value) + ",", end="")
            currNode = currNode.next
        print(str(currNode.value) + "]")
    
    def pop(self, index = -1):
        currNode = self.root
        
        if index == 0:
            self.root = self.root.next
            
            if self.root == None:
                self.setRoot(LinkedNode(None))
            
            return currNode
        
        if index > 0:
            for i in range(index):
                currNode = currNode.next
        else:
            currNode = self.getLastNode()
            
        currNode.previous.next = currNode.next
        return currNode