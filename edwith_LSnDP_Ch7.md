[EDWITH: Linear Structure and Dynamic Programming](https://www.edwith.org/datastructure-2019s)    
Chapter 7: Algorithm Analysis
# What is the Algorithm?
- A clearly specified set of simple instructions to be followed to solve a problem
- Take input -> give output
- Program is a combination of algorithm and data structures
- Examples of algorithms...
	- insertion, deletion, search, stack, queue, **sorting**, ...
	- Examples of **sorting** algorithm
		- Bubble sort, Quick sort, Merge sort, ...
# Example of algorithm: Bubble Sort Algorithm
- Bubble Sort Algorithm is a simple and basic sorting algorithm
- The algorithm to sort the list in descending order
- Let's say we have a list, $[3, 2, 1, 5, 4]$
	- compare the first element($3$) with rest of them, one by one, following the list
	- when you find the bigger element, exchange the location of them
	- If you reach to the end, start from the second element

| | | | | | |
|:-:|:-:|:-:|:-:|:-:|:-|
|3*|2|1|5*|4| 3 is smaller than 5. Exchange the location.|
|5*|2|1|3|4| nothing is smller than 5.|
|5|2*|1|3*|4|2 is smaller than 3. Exchange the location.|
|5|3*|1|2|4*|3 is smaller than 4. Exchange the location.|
|5|4*|1|2|3|nothing is smller than 4.|
|5|4|1*|2*|3|1 is smaller than 2. Exchange the location.
|5|4|2*|1|3*|2 is smaller than 3. Exchange the location.
|5|4|3*|1|2|nothing is smller than 3.|
|5|4|3|2*|1|nothing is smller than 2.|

- We can describe the algorithm in pseudo code
```
for itr1 = 0 to length(list)
	for itr2 = itr + 1 to length(list)
		if list[itr1] < list[itr2]
			swap list[itr1], list[itr2]
return list
```
- Now, we can pratice this pseudo code into practical python code
## Python practice
```python
import random

def performSelectionSort(lst):
    for itr1 in range(0, len(lst)):
        for itr2 in range(itr1+1, len(lst)):
            if lst[itr1] < lst[itr2]:
                lst[itr1], lst[itr2] = lst[itr2], lst[itr1]
    return lst


N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)
print(lstNumbers)
print(performSelectionSort(lstNumbers))


lstNumbers2 = [2, 5, 0, 3, 3, 3, 1, 5, 4, 2]
print(lstNumbers2) #[[2, 5, 0, 3, 3, 3, 1, 5, 4, 2]
print(performSelectionSort(lstNumbers2)) #[5, 5, 4, 3, 3, 3, 2, 2, 1, 0]
```

# Algorithm Efficiency
- Program could be **inefficient**
	- Large data -> running time becomes a big issue
- We need a gurantee of the worst-case scenario
	- Worst-case running time of a single transaction
	- Worst-case transaction request numbers of a single day
# Algorithm Analysis
- Estimate the resources like...
	- Memory
	- Communication bandwidth
	- **Computational time**
- Factors affecting the running time
	- Computer used for executions
	- Algorithms
	- Data structures
	- Input data size
- After analyzing the algorithms
	- Estimate the worst-case of the costs by the factors
## Simple algorithm analysis
- Caculate the iteration of each line
```python
def calculateIntegerRangeSum(intFrom, intTo):
	intSum=0 # iteration: 1

	for itr in range(intFrom, intTo): # iteration: N
		intSum = intSUm + itr # iteration: N

	return intSum # iteration: 1

print(calculateInegerRangeSum(0,10))
```
- Total iteration    
  = 1 + N + N + 1    
  = 2N + 2
# Big O notation
- One example of asymptotic notation .
- Show the worst-case running time
$$\huge f(N) = O(g(N))$$
- There are positive constants $c$, and $n_0$.
  when $N ≥ n_0$,
$$\huge f(N) ≤ c＊g(N)$$
 - Big O notation ignores the lower-order terms, and the constants(coefficients) of highest-order term
	 - When we have $N^3$, $N^2$ and $N$ means nothing in terms of Big O
	 - From the growth rate order    
		   $\huge C^N > N^K > N^2 > NlogN > N > logN > C$
		   $C≥2$ and $K>2$
	 - Therefore, given example of simple algorithm analysis' total iteration $2N+2$ turns into $O(N)$. The constant term $2N$ are disregarded, leaving only the $N$ term in the Big O notation.
 
 - The growth rate of $f(N)$ is less than or equal to the growth rate of  $g(N)$
 - $g(N)$ is an uppder bound on $f(N)$

## Analysis the Bio-O of Bubble Sort Algorithm
```python
def performSelectionSort(lst):
    for itr1 in range(0, len(lst)): # iteration: N
        for itr2 in range(itr1+1, len(lst)): # iteration: N-i
            if lst[itr1] < lst[itr2]: 
                lst[itr1], lst[itr2] = lst[itr2], lst[itr1]
                
    return lst # iteration: 1
```
- $N$ is the length of the list.
- About the second $for$ loop, `for itr2 in range(itr1+1, len(lst))` 
	- To calculate the efficiency, worst case should be considered.
		- Assume that $for$ loops will reach to the end without problems, and $if$ always results in true
	- How many items will be given from the second $for$ loop?
		- Consider the frst $for$ loop together
		- `for itr1 in range(0, len(lst)`    
		   $\huge \sum_{i=0}^{N-1}$ 
		- `for itr2 in range(itr1+1, len(lst)`    
		  $\huge \sum_{j=i+1}^{N-1}$ 
		$$\huge \sum_{i=0}^{N-1} \sum_{j=i+1}^{N-1} 1= {1 \over 2}n^2 - {1 \over 2}n$$
	- for single item from `for itr2 in range(itr1+1, len(lst)`,    
	  3 iterations are needed
		1) for itr2 in range(itr1+1, len(lst)
		2) if lst[itr1] < lst[itr2] :
		3) lst[itr1], lst[itr2] = lst[itr2], lst[itr1]
	- Therefore, the iteration for the second $for$ loop multiple three times
- Total iteration    
  = $\huge n + ({1 \over 2}n^2-{1 \over 2}n)3 + 1$
   
   >Big O notation ignores constants and lower-order terms.
   
   = $\huge O(N^2)$

## Examples of Big O notation
$$ O({N^2 \over 2-3N}) = O(N^2)$$

$$O(1+4N) = O(N)$$

$$O(7N^2 + 1-N + 3) =O(N^2)$$

$$\begin{align}
\huge O(logN)=O(log_{2}N) \\
(log_{10}N = {{log_{2}N} \over {log_{2}10}}) \\
\end{align}$$

$$O(sinN) = O(1)$$

$$ O(10) = O(1)$$

$$O(10^10)=O(1)$$

$$O(log{N}+N)=O(N)$$
## Big O notation of list, stack, and queue
| | List | Stack | Queue |
|:-:|:-:|:-:|:-:|
|pop|X|1 retrieval<br>$O(1)$|X
|Push|X|1 retrieval<br>$O(1)$|X|
|Enqueue|X|X|1 retrieval<br>$O(1)$|
|Dequeue|X|X|1 retrieval<br>$O(1)$|
|Search|$i$ retrieval<br>(if the target instance<br>at $i^th$ in the list)<br>$O(N)$|X<br>(Does not allow search<br>in the stack)|X<br>(Does not allow search<br>in the queue)|
