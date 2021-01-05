from SingleLinkedList import SinglyLinkedList

if __name__ == "__main__":
    #Create list and add to it
    linkedList = SinglyLinkedList("Apple")
    linkedList.append("Banana")
    linkedList.append("Cream")
    linkedList.append("Daikon")
    linkedList.append("Edamame")
    linkedList.append("Fig")
    linkedList.append("Grape")
    #Print to check
    print(linkedList.getLastNode().value)
    linkedList.printList()
    
    #Pop element
    print(linkedList.pop().value)
    #Print to check
    linkedList.printList()
    
    #Pop element
    print(linkedList.pop(2).value)
    #Print to check
    linkedList.printList()