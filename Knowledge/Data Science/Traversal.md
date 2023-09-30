- Queue, Stack으로 대표되는 linear data structure와 Tree data structure는 모든 node들을 '방문'하는 방법에서 큰 차이를 보여준다.
- Linear data structure의 경우 모든 node를 방문하는 방법은 한가지 방법 뿐이다. 데이터 구조가 일자로 뻗은 선형이기 때문에, 처음 node부터 마지막 node까지 순서대로 거쳐가며 방문하면 된다.
- 반면에 Tree data structure의 경우, 각 node에 분기가 있기 때문에 모든 node를 방문하는 방법이 다양해질 수 밖에 없다. 더 이상 분기가 없는 가장 바닥의 node까지 방문한 다음 뒤로 돌아오는 방법도 있을 것이고, 분기에서 만난 node들만 방문하고서 한 분기를 선택해 계속 방문해가는 방법도 있을 것이다.
- 이렇게 tree data structre에서 모든 node들을 방문하는 것을 traversal(순회)이라고 부른다.
- Tree data structure를 배울 때는 일반적으로 Binary Search Trees(BST)를 상상하고 공부한다.
	- BST의 경우 각 node는 최대 두 개의 분기를 가진다.
- Tree data structure는 크게 4가지의 방식으로 traverse가 가능하다.
	1. Depth First Search([[DFS]])
		- Inorder Traversal
		- Preorder Traversal
		- Postorder Traversal
	2. Level Order Traversal or Breadth First Search or [[BFS]]
	3. Boundary Traversal
	4. Diagonal Traversal
## 1. DFS
- DFS는 깊이우선탐색으로, tree structure의 가장 바닥이 어디인지 빠르게 파악하는데 도움을 준다.
- DFS를 활용한 traversal의 경우, 어디를 방문 시작점으로 잡느냐에 따라 결과물이 달라진다.
	- 가장 왼쪽 끝의 node부터 시작해서 순서대로 올라가는 경우(inorder)
	- 맨 위의 node에서부터 시작하는 경우(preorder)
	- 가장 왼쪽 끝의 node부터 시작하되, 바닥의 node들을 다 탐색하며 올라오는 경우(postorder)
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230623123129/traversal.png">

- **다시금 말하지만 DFS에서 중요한 것은 '가장 바닥이 어디인지', '이 tree구조의 깊이가 얼마나 되는지' 빨리 파악하는 것에 초점을 둔다.**
- 위의 그림에서 가장 왼쪽 끝 바닥의 node인 4의 위치가 항상 앞쪽에 나열된다는 점에 주목하자.
### DFS를 이용한 Inorder Traversal, Preorder Traversal, Postorder Traversal의 구현
```python
# Binary Search Tree(BST) Structure

# 0. Build BST node
Class Node:
	def __init__(self, key):
		self.left = None # child 1
		self. right = None # child 2
		self.val = key

# 1. Inorder Traversal
def printInorder(root):
	if root:
		printInorder(root.left) # Recursive Function. Keep go to left!
		print(root.val, end=" ") # Come back to root
		printInorder(root.right) # Go to right
		
# 2. Preorder Traversal
def printPreorder(root):
	if root:
		print(root.val, end=" ") # Root First
		printPreorder(root.left) # Recursive Function. Keep go to left!
		printPreorder(root.right) # Now go to right

# 3. Postorder Traversal
def printPostorder(root):
	if root:
		printPostorder(root.left) # Recursive Function. Keep go to left!
		printPostorder(root.right) # Go to right
		print(root.val, end=" ") # Check the root as last
		
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Inorder traversal of binary tree is")
    printInorder(root) # 42513
    print("Preorder traversal of binary tree is")
    printPreorder(root) # 12453
    print("Postorder traversal of binary tree is")
    printPostorder(root) # 45231
```
## 2. BFS

## 3. Boundary Traversal
## 4. Diagonal Traversal

## 참조
- https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/