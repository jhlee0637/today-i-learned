[EDWITH: Linear Structure and Dynamic Programming](www.edwith.org/datastructure-2019s) Chapter 3
# Abstract Data Types(ADT)
- An abstraction of a data structure
- Include...
	- Stack
	- Queue
	- List
	  ...
- ADT specifies...
	- Data stored
	- Operations on the data
	- Error conditions associated with operations
		- Error condition: expect future error and plan the solution
# What is *array* in general programming
- Array has elements
- The elements is accessible by index
- The index is typically zero or a positive integer
## Search procedure in *array* and  retrieval time
- Should use indexes only for searching
1) Navigate from the first
2) Keep navigate until hit
	- If there is no hit, reach to the end
- The maximum retrievals are **N**
## Insert procedure in *array* and  retrieval time
- We have list 'X'
- Want to insert 'c' in third place
1) Create a new empty list 'Y'
2) Put first and second elements of 'X' to 'Y'
3) Put 'c' to 'Y'
4) Put rest elements of 'X' to 'Y'
5) Claim, 'X = Y'
- Have to reach to the end of 'X', therefore, the retrievals are N
## Delete procedire in *array* and retrieval time
- We have list 'X'
- Want to delete 'd' in fourth place
1) Create a new empty list 'Y'
2) Put first to thrid elements of 'X' to 'Y'
3) Do not input 'd' from 'X' to 'Y'
4) Put rest elements of 'X' to 'Y'
5) Claim, 'X = Y'
- Have to reach to the end of 'X', except one element
- The retrievals are N-1, almost same as N
## The problems in *array*
- Have to perform line-wise retrievals, N retrievals
- So, the procedure are bounded to the one-dimension
- **What if we have a magic to create a space in the middel of the line?**
	- ***Linket list*** -> the procedure is not bounded anymore -> solve!
# Singly Linked List
- A singly linked list is organized with nodes and references
## Node
- A node consists of
	1) A variable to hold a reference to its next node
	2) A variable to hold a reference to its value object
- There are two special nodes: *Head, Tail*
	- *Head* is the first node of the list, *Tail* is the last node of the list
	- Special nodes don't have references, no need to connect to the next node
		- *Head* doesn't have value
		- *Tail* doesn't have value and next node linkage
	- Special nodes are necessary to a linked list.
	  However, they make procedures more convenient such as search, insert, and delete
## Reference
- The node's variables are linked with references
- Reference can be a value or next node
## Practice
```python
'''
Singly linked list: a type of data structure.
                    It's built with several nodes.
                    Each nodes are linked with their own reference values. (except head and tail nodes)

Before we implement a singly linked list,
we should define the Node class.
'''
class Node:
    nodeNext = None
    nodePrev = ''
    objValue = ''
    blnHead = False #head and tail nodes are optional.
    blnTail = False #having head and tail makes implementation very convenient.
    
    def __init__(self, objValue='', nodeNext = None, blnHead = False, blnTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.blnHead = blnHead
        self.blnTail =blnTail
    
    def getValue(self): #node has a variable to it's reference value
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue

    def getNext(self): #node has a variable to it's next node
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext

    def isHead(self):
        return self.blnHead
    def isTail(self):
        return self.blnTail

node1 = Node(objValue = 'a')
nodeTail = Node(blnTail = True)
nodeHead = Node(blnHead = True, nodeNext = node1)
```
# Search Procedure in Singly Linked List
- Actually, searching procedure in singly linked list takes time as much as array
- Check every values
- The procedure is like....
	1) Find Head node
	2) Loop to search next node
		- if Tail node -> exit
		- if not Tail node -> value check
# Insert&Delete Procedure in Singly Linked List
- Insert and Delete procedures takes much less time than array
## Insert Procedure
- Let's say, we already have a new node which we want to insert
- Let's say, put node 'c', between 'a'-'b'-'d'-'e'
1) Find previous node(node 'b')
2) Link the next variable of the previous node, to the new node(node 'b' -> node 'c')
3) Modify the next variable of the new node, to the next node(node 'c' -> node 'd')
## Delete Procedure
1) Retrieve a new next node, which is two nodes far from a previous node
3) Change a reference of the next variable in a previous node, to the new next node
## Practice
```python
'''
Implement singly linked list using the node class we definied.
We can do insertion or deletion of nodes from singly link list.

1) Insert procedure: store the new node
                     update the previous node to point the new node
                     update the new node to point the next node

2) Delete procedure: retrieve the next node
                     update the previous node to point the next node
'''
from ImportOnly.NodeClass import Node 

class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeTail = Node(blnTail=True)
        self.nodeHead = Node(blnHead=True, nodeNext = self.nodeTail)

    def insertAt(self, objInsert, idxInsert): 
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1) #get the previous node through the method 'get' which is defined from below
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()

    def get(self, idxRetrieve): #method 'get' to get which index's node
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end=" ")
        print("")

    def getSize(self):
        return self.size

'''
Let's try:  a - b - d - e - f

            a - b -"c"- d - e - f

            a - b - c ----- e - f
'''
list1 = SinglyLinkedList()
list1.insertAt('a',0)
list1.insertAt('b',1)
list1.insertAt('d',2)
list1.insertAt('e',3)
list1.insertAt('f',4)
list1.printStatus()

list1.insertAt('c',2) #insert the node at the middle of the array
list1.printStatus()

list1.removeAt(3) #delete the node at the middle of the array 
list1.printStatus()
```
# Stack
## Structure of *Stack*
- Stacks are linear like linked lists
	- A variation of a singly linked list
- You can only access to **the first instance** in the list
	- This mechanism is called Last-In-First-Out(LIFO)
	- You cannot modify other instances in the list
- Imagine the snack, Pringles
	- You can only access to the top of the container
## *Push* operation of *Stack*
- Insert an instance at the first in the linked list
- Put an instance at the top in the stack
## Pop operation of Stack
- Remove and return an instance at the first in the linked list
- Remove and return an instance at the top in the stack
## Practice
```python
'''
Stacks are the name of data structure.
Stacks are linear like linked lists.
You can only access to the end of stack.
You can't insert or delete the data from middle. (Last In First Out)

Stack has two operations.
1) Push: insert an instance at the first in the linked list.
2) Pop: remove and return an instance at the first in the linked list.
'''
from ImportOnly.SinglyLinkedList import SinglyLinkedList

class Stack(object):
    lstInstance = SinglyLinkedList()

    def pop(self):
        return self.lstInstance.removeAt(0) #remove from first

    def push(self, value):
        self.lstInstance.insertAt(value, 0) #insert to first

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

print(stack.pop()) #c
print(stack.pop()) #b
print(stack.pop()) #a
```
## Where to use *Stack* structure?
- For example, check balancing symbols
	- Balancing symbols: ( ), { }, [ ]
	- `[2+(1+2)]-3` -> balanced symbols
	- `{2+(1}+2)-3` -> not balanced symbols
- It's not about counting symbols
- It's about opening and closing at right order
- Algorithm for the balanced symbol checking
	1) Make an empty stack
	2) Read symbols until end of formula
		- If the symbol is an opening symbol, push it onto the stack
		- If the symbol is a closing symbol
			- If the stack is empty -> error
			- If the stack has matched symbol -> pop
			- If the stack has not-matched symbol -> error
	3) At the end of the formula, if the stack is not empty -> error
# Queue
## Structure of Queue
- Queues are linear like linked lists
	- A variation of a singly linked list
- You can only access to **the first and last instance** in the list
	- This mechanism is called First-In-First-Out(LIFO)
	- You cannot modify other instances in the list
- Items are inserted at the last, removed at the front
## Enqueue operation from Queue
- Insert an instance at the last in the linked list
- Put an instance at the rear in the queue
## Dequeue operation from Queue
- Remove and return an instance at the first in the linked list
- Remove and return an instance at the front in the queue
## Practice
```python
'''
Queues are the name of data structure.
Queues are linear like linked lists.
You can insert to the first of queue.
You can remove from the end of queue.
You can't insert or delete the data from middle. (First In First Out)

Queue has two operations.
1) Enqueue: insert an instance at the last in the linked list.
2) Dequeue: remove and return an instance at the first in the linked list.
'''
from ImportOnly.SinglyLinkedList import SinglyLinkedList

class Queue(object):
    lstInstance = SinglyLinkedList()

    def dequeue(self):
        return self.lstInstance.removeAt(0) #remove from first

    def enqueue(self, value):
        self.lstInstance.insertAt(value, self.lstInstance.getSize()) #insert to end

queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print (queue.dequeue()) #a
print (queue.dequeue()) #b
print (queue.dequeue()) #c
```