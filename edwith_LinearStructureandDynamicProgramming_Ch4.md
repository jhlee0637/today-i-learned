# Recursion
## Repeating Problem from Programming
1) You use a method to solve problem, get a value
2) Now, you have to use the value to put it in the same method, and get another value
3) repeating...
- The size of problem decreases
- Examples
	- Factorial
	- Great Common Divisor
		- GCD(32, 24) = 8
		- Using Euclid's algorithm
		  GCD(A, B) = GCD(B, A mod B)
		  GCD(A, 0) = A
- Commonality
	- Repeating function calls
	- Reducing parameters
	- Just like the mathematical induction
## Using Recursion to handle the Repeating Items
- Often in a form of calling a function within the function
## Practice: Fibonacci
```python
'''
Recursion: A programming method to handle the repeating items in a 'self-similar' way.
           often calling the function again within the function.
'''

def Fibonacci(n):
    if n == 0: #escape when it's not for recursion
        return 0
    if n == 1: #escape when it's not for recursion
        return 1
    intRet = Fibonacci(n-1) + Fibonacci(n-2) #calling the function again within the function
    return intRet

for itr in range(0, 10):
    print(Fibonacci(itr), end=" ") #0 1 1 2 3 5 8 13 21 34
```
# Stackframe
- *Recursion* is a repeat of function call
- *Stackframe* is a stack storing your function call history
- Two types of *Stackframe*'s actions
	- *Push*: When a function is invoked, **record the function call**
	- *Pop*: When a function hits *return* or ends, **remove the function call**

# Merge Sort
- *Merge Sort* is one example of recursive programming
	- Sorting randomly aligned numbers in ascending order 
	- Convert this problem into repeating problem -> decompose and aggregate
## Merge Sort Procedures
- Decompose into two smaller lists
- Compare two smallest lists
- Aggregate to one larger and sorted list
- Repeat Comparision and Aggregattion
## Practice
```python
'''
Merge sort is an example of recursive programming.
It's a way of sort of the list.
Repeatedly decompose the list into two smaller lists.
When you can't divide the list anymore, aggregate to one sorted list.
'''

import random

def perfomrMergeSort(lstElementToSort):
    if len(lstElementToSort) == 1: #escape when the list not for recursion
        return lstElementToSort

    #decompose of the given list
    lstSubElementToSort1 = [] 
    lstSubElementToSort2 = []
    for itr in range(len(lstElementToSort)):
        if len(lstElementToSort)/2 > itr:
            lstSubElementToSort1.append(lstElementToSort[itr])
        else:
            lstSubElementToSort2.append(lstElementToSort[itr])

    #recursion - repeatedly decompose the list until it can't be divded anymore
    lstSubElementToSort1 = perfomrMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = perfomrMergeSort(lstSubElementToSort2)

    #aggregate
    idxCount1 = 0
    idxCount2 = 0
    for itr in range(len(lstElementToSort)):
        if idxCount1 == len(lstSubElementToSort1):
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        elif idxCount2 == len(lstSubElementToSort2):
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
        elif lstSubElementToSort1[idxCount1] > lstSubElementToSort2[idxCount2]:
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        else:
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
    
    return lstElementToSort

#Test
lstRandom = []
for itr in range(0, 10):
    lstRandom.append(random.randrange(0, 100))
print(lstRandom)

lstRandom = perfomrMergeSort(lstRandom)
print(lstRandom)
```
# Question: Is Recursion really good?
- Cons: longer list needs more time and space
	- Excessive function calls
	- Same funcions can be overlapped
		- For, instance, Fibonacci(4)
		  F(4) = F(3) + F(2)
			  = F(2) + F(1) + F(1) + F(0)
			  = F(1) + F(0) + F(1) + F(1) + F(0)
		- Fibonacci(4) has three repeated calls of F(1), two repeated F(0), two repeated F(2)
- Solution -> ***Dynamic Programming***