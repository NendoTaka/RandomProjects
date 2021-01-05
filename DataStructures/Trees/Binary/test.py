from BinaryTree import BinaryTree

if __name__ == "__main__":
    #Create list and add to it
    binaryTree = BinaryTree("Apple")
    binaryTree.append("Banana")
    binaryTree.append("Cream")
    binaryTree.append("Daikon")
    binaryTree.append("Edamame")
    binaryTree.append("Fig")
    binaryTree.append("Grape")
    #Print to check
    print("Tree 1 ---------------")
    binaryTree.printTree()
    
    #Create list and add to it
    binaryTree = BinaryTree("Daikon")
    binaryTree.append("Banana")
    binaryTree.append("Cream")
    binaryTree.append("Apple")
    binaryTree.append("Fig")
    binaryTree.append("Edamame")
    binaryTree.append("Grape")
    #Print to check
    print("Tree 2 ---------------")
    binaryTree.printTree()
