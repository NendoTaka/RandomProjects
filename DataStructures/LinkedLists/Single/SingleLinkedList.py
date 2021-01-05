from Node import LinkedNode

class SinglyLinkedList:
    def __init__(self, value):
        self.setRoot(LinkedNode(value))
        
    def setRoot(self, node):
        self.root = node
    
    def append(self, value):
        lastNode = self.getLastNode()
        lastNode.next = LinkedNode(value)
        
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
        previousNode = None
        currNode = self.root
        
        if index == 0:
            self.root = self.root.next
            
            if self.root == None:
                self.setRoot(LinkedNode(None))
            
            return currNode
        
        if index > 0:
            for i in range(index):
                previousNode = currNode
                currNode = currNode.next
        else:
            while currNode.next != None:
                previousNode = currNode
                currNode = currNode.next
            
        previousNode.next = currNode.next
        return currNode