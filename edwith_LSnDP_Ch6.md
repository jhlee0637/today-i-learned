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
- Linked List is linear structure, each node has one single 'next' variable
	■ ─ ■ ─ ■ ─ ■
- One Tree's node could have multiple 'next' variables
	■  ┬ ■
	  ├ ■
	  ├ ■
	  └ ■
- Particularly, the structure maintains the next nodes as an array or variables
## Some terms of *Tree* structure
- Root: the toppest node
- Edge: the line from a node to the next node
- Parent-Child: When two nodes are linked through the edge, they are in Parent-Child relationship
- Siblings: a group of Child nodes
- Leave nodes/Terminal nodes: the nodes at bottom
- Internal nodes: nodes between Leave and Root
- Path to 'x': the shortest way from Root to the node 'x'
- Ancestors of 'x': Every ancestor nodes of the node 'x'
- Descendants of 'x': Every descendants nodes of the node 'x'
- Size of tree: the number of all nodes
- Depth and level of 'x': same as 'Path'
- Height: the maximum depth of the Tree structure
- Degree of 'x': the maximum nodes which the node 'x' could acquire