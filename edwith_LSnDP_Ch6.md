[EDWITH: Linear Structure and Dynamic Programming](www.edwith.org/datastructure-2019s)   
Chapter 6: Tree
# *Tree* Structure is an abstract data type
## *Abstract Data Type*
- *ADT* is specified in
	- Data stored
	- Operations on the data
	- Error conditions associated with operations
## *Tree* as an abstract data type
- Data is stored as a *Tree* structure
- Operations on the data are...
	- including ordinary data structure's operations such as
		*- Insert
		- Delete
		- Search*
	- In addition, *Tree* structure has a special operation called
		- *Traverse*: Special searching approaches for trees and networks
## Why do we use *Tree*?
- *Tree* structure is good analogy to the various real world structures
	- Corporate structrues
	- Group bank accounts
	- Command and control structures
- *Tree* structure is easy to *Divide* and *Conquer* the data
## Compare with *Linked List* and *Tree*
- Linked List is linear structure, one Linked List node has single 'next' variable
- One Tree node can have multiple 'next' variables   
- Particularly, the structure maintains the next nodes as an array or variables
# Some terms of *Tree* structure
- Root: the toppest node
- Edge: the line from a node to the next node
- Parent-Child: When two nodes are linked through the edge, they are in Parent-Child relationship
- Siblings: a group of Child nodes
- Leave nodes/Terminal nodes: the nodes at bottom
- Internal nodes: nodes between Leave and Root
## *Ancestors, Descendants, Path*
- Ancestors of 'x': Every ancestor nodes of the node 'x'
- Descendants of 'x': Every descendants nodes of the node 'x'
- Path to 'x': the shortest way from Root to the node 'x'
## *Depth, Size, Height, Degree*
- Depth and level of 'x': same as 'Path'
- Size of tree: same as many as nodes
- Height: the maximum depth of the Tree structure
- Degree of 'x': the maximum nodes which the node 'x' could acquire
## *Full Tree* and *Complete Tree*
-  Ful Tree: utilize every next nodes. 
	- Tree height = Tree depth
- Complete Tree: the next nodes are not fully utilized yet
	- The nodes are filled from the left side of the graphic of the structure
# Characteristics of Tree
- {Number of edges} = {Number of nodes } - 1
- {Depth of Root} = 0
- {Maximum number of nodes at level *i* with degree *d*} = *d*$^i$ 
- {Maximum number of leaves with height *h* and degree *d*} = *d*$^ h$
- {Maximum size of a tree with height *h* and degree *d*} = 1 + *d* + *d*$^ 2$ + *d*$^ 3$ + ... + *d*$^ h$
- {Height of a complete tree with size *s* and degree *d*} = [log$ d$(*s*(*d* - 1) + 1] - 1
# *Binary Search Tree*(*BST*)
## *Binary Tree* vs *Binary 'search' Tree*
- *Binary Tree* is a tree structure with degree 2
- *Binary Search Tree* is a tree structure with degree 2, and designed for a **fast search** of stored data
## How to perform a faster search from Binary Search Tree?
- Single tree node can be linked to several different tree nodes
- It does not need to search as long as the length of data
## Let's code Tree node
- This time, we will design Tree node has two next variables
	- Left hand side (LHS): usually to lower value
	- Right hand side (RHS): usually to higher value
- Tree node have its own value
- Tree node have its parent node
```python
'''
Tree structure is a type of an adstract data type. (Same as like stack, queue, ...)
Tree structure has operations, 'insert', 'delete', 'research'.
    Tree structure has special search approach called 'Traverse'

Compare with the Singly linked list, Tree structure's node involves several 'next nodes' pointing the next node.
Let's build a node for tree structure within two next nodes.
'''
class TreeNode:
    nodeLHS = None #next node1: Left hand side - when values have "lower" than it's own value
    nodeRHS = None #next node2: Right hand side - when values have "higher" than it's own value
    nodeParent = None #previous node
    value = None

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS
    def getRHS(self):
        return self.nodeRHS
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent

    def setLHS(self, LHS):
        self.nodeLHS = LHS
    def setRHS(self, RHS):
        self.nodeRHS = RHS
    def setValue(self, value):
        self.value = value
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent
```
# *BST*'s operations
- *BST* handles thedata sotred throught its root
	- *Root* has its own value
	- *Tree* instance access to the *Root*
	- Only through the *Root*, the *Tree* instances access to the descendant nodes of the *Root*
## Insert operation
- Retrieve the current node value
- If the value is...
	- ...equal to the value to insert
		- Return
	- ...smaller to the value to insert
		- If there is a node in the RHS -> move to RHS (Recursion)
		- If there is no node in the RHS -> create RHS node -> insert the value
	- ...larger to the value to insert
		- If there is a node in the LHS -> move to LHS (Recursion)
		- If there is no node in the LHS -> create LHS node -> insert the value
## Search operation
- Retrieve the current node value
- IF the value is...
	- ...equal t the value to search
		- Return **True**
	- ...smaller to the value to insert
		- If there is a node in the RHS -> move to RHS (Recursion)
		- If there is no node in the RHS -> return **False**
	- ...larger to the value to insert
		- If there is a node in the LHS -> move to LHS (Recursion)
		- If there is no node in the LHS -> return **False**
## Delete operation
- Delete operation can be under three cases
	1) Case1. deleting a node with no children
	2) Case2. deleting a node with 1 child
	3) Case3. deleting a node with 2 children
### Case1. deleting a node with no children
- Just remove the node by modifying its parent
### Case2. deleting a node with 1 child
- Replace the node with the child
### Case3. deleting a node with 2 children
- Find either
	- A maximum in the LHS or RHS
	- Substitute the node to delete with the found value
	- Delete the found node in the LHS or RHS
- The Tree structure can be looked different after the delete operation which you choosed between LHS or RHS
## Escape
- In a recursive function, there must be a termination condition that allows the function to exit without calling itself. 
## Practice(BST, Insert, Search, Delete, find)
```python
'''
Binary Search Tree(BST) is one of the simplest tree structure.
Each node from BST is built within two next nodes, as like the tree node we just built from '6_1_TreeStructure_TreeNode.py'

Let's implement BST with the several operations(insert, delete, search, travse, ...)
'''
from ImportOnly.TreeNode import TreeNode #please check https://github.com/jhlee0637/CodeExercising
from queue import Queue

class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value, node = None):
        if node is None:
            node = self.root
        #Before insertion, the operation to look for a place to insert is run by recursions. -> so we write down 'escape route' from the recursions on here.
        if self.root is None:
            self.root = TreeNode(value, None) #if there is no root, you are the root now
            return
        if value == node.getValue(): #if the value is equal to the vaule to insert
            return #return already there
        #try to insert to RHS
        if value > node.getValue(): #if the value is smaller than the value to insert, try to insert to RHS
            if node.getRHS() is None:
                node.setRHS(TreeNode(value, node)) #insert to RHS
            else:
                self.insert(value, node.getRHS()) #if RHS is not empty, recursion(go down to the next level of that RHS)
        #try to insert to LHS
        if value < node.getValue():
            if node.getLHS() is None:
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.hetHLS)

    def search(self, value, node = None):
        #initiating from a root
        if node is None: 
            node = self.root
        #Searching uses recursion too -> we need 'escape' in here too.
        if value == node.getValue():
            return True
        #search from the RHS
        if value > node.getValue(): #if the value is smaller than the value to search, look at the RHS
            if node.getRHS() is None:
                return False #if there is no node in RHS, FALSE
            else:
                return self.search(value, node.getRHS()) #if there is node, recursion
        #search from the LHS
        if value < node.getValue():
            if node.getLHS() is None:
                return False
            else:
                return self.search(value, node.getLHS()) #recursion
        
    def delete(self, value, node = None):
        #initiating from a root
        if node is None:
            node = self.root
        #find a node to delete through recursions
        if node.getValue() < value:
            return self.delete(value, node.getRHS())
        if node.getValue() > value:
            return self.delete(value, node.getLHS())
        #there are three cases to delete node from the BST
        if node.getValue() == value:
            if node.getLHS() is not None and node.getRHS() is not None: #case1) the node has both LHS and RHS -> we can choose one of them to replace the deleted node. -> Let's choose RHS -> the minium value from RHS's childs will replace the current value.
                nodeMin = self.findMin(node.getRHS) #function 'findMin' will be defined later.
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                return
            parent = node.getParent()
            if node.getLHS() is not None: #case2) the node has one child(LHS)
                if node == self.root:
                    self.root = node.getLHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            if node.getRHS() is not None: #case2) the node has one child(RHS)
                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                return
            if node == self.root: #case3) if there are no childs
                self.root = None
            elif parent.getLHS() == node:
                parent.setLHS(None)
            else:
                parent.setRHS(None)
            return

    def findMax(self, node = None): #the end of RHS is the maximum - keep recursion
        if node is None:
            node - self.root
        if node.getRHS() is None:
            return node
        return self.findMax(node.getRHS())

    def findMin(self, node = None): #the end of LHS is the minimum - keep recursion
        if node is None:
            node = self.root
        if node.getLHS() is None:
            return node
        return self.findMin(node.getLHS())
    
    '''
    Tree traversing: Tree structure has several ways of traversing
        Breadth first traverse: 1) Queue-based lavel-order traverse
        Depth first traverse: 1) Pre-order traverse, 2) In-order traverse, 3) Post-order traverse
    '''
    def traverseLevelOrder(self): #Breaadth first traverse
        ret = []
        Q = Queue()
        Q.enqueue(self.root)
        while not Q.isEmpty(): #enqueue the root while until queue is empty
            node = Q.dequeue()
            if node is None:
                continue
            ret.append(node.getValue())
            if node.getLHS() is not None: #if current's LHS exist -> enqueue current LHS
                Q.enqueue(node.getLHS()) 
            if node.getRHS() is not None: #if current's RHS exist -> enqueue current RHS
                Q.enqueue(node.getRHS())
        return ret
    
    def traverseInOrder(self, node = None): #In-order traverse
        if node is None: #Recursion -> need exigt
            node = self.root
        ret = []
        if node.getLHS() is not None: #Put LHS first
            ret = ret + self.traverseInOrder(node.getLHS())
        ret.append(node.getValue()) #Put current second
        if node.getRHS() is not None: #Put RHS last
            ret = ret + self.traverseInOrder(node.getRHS())
        return ret
    
    def traversePreOrder(self, node = None): #Pre-order traverse
        if node is None: #Recursion -> need exigt
            node = self.root
        ret = []
        ret.append(node.getValue()) #Put current first
        if node.getLHS() is not None: #Put LHS second
            ret = ret + self.traversePreOrder(node.getLHS())
        if node.getRHS() is not None: #Put RHS last
            ret = ret + self.traversePreOrder(node.getRHS())
        return ret
    
    def traversePostOrder(self, node = None): #Post-order traverse
        if node is None: #Recursion -> need exigt
            node = self.root
        ret = []
        if node.getLHS() is not None: #Put LHS first
            ret = ret + self.traversePostOrder(node.getLHS())
        if node.getRHS() is not None: #Put RHS second
            ret = ret + self.traversePostOrder(node.getRHS())
        ret.append(node.getValue()) #Put current last
        return ret

```
# Performance of *Binary Search Tree*

| |Linked List|BST in Average|BST in Worst Case|
|:---:|:---:|:---:|:---:|
|Search|O(n)|O(log n)|O(n)|
|Insert after search|O(1)|O(1)|O(1)|
|Delete after search|O(1)|O(1)|O(1)|
|Traverse|O(n)|O(n)|O(n)|
- What is the 'BST in Worst Case'?
	- Imagine the tree structure which every nodes have only single next node
	- The structure would be looked like a list
- At 'Search', 'BST in Average' has O(log n) while 'BST in Worst case' has O(n)
	- This is coming from divide and conquer
	- Heigh confirms the performance