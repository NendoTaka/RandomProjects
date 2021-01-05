class LinkedNode:
    def __init__(self, value, previousNode):
        self.next = None
        self.previous = previousNode
        self.value = value
    
    def setNext(self, nextNode):
        self.next = nextNode
        
    def setPrevious(self, previousNode):
        self.previous = previousNode
    
    def setValue(self, value):
        self.value = value