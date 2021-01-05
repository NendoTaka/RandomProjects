class LinkedNode:
    def __init__(self, value):
        self.next = None
        self.value = value
    
    def setNext(self, nextNode):
        self.next = nextNode