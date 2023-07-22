[EDWITH: Linear Structure and Dynamic Programming](https://www.edwith.org/datastructure-2019s)    
Chapter 7: Algorithm Analysis
# What is the Algorithm?
- A clearly specified set of simple instructions to be followed to solve a problem
	- input -> output
- Specified in verbal language, computer program, Pseudo-code
	- Program = algorithm + data structures
- Examples of algorithms
	- insertion, deletion, search, stack, queue, sorting, ...
	- Examples of Sorting algorithm
		- Bubble sort, Quick sort, Merge sort, ...
# Example of algorithm: Bubble Sort Algorithm
- Bubble Sort Algorithm is a simple and basic sorting algorithm
- Let's say we have list [3, 2, 1, 5, 4]
	- compare the first element(3) with rest of them one by one, following the list
	- when you find the bigger element, exchange the location of them
	- If you reach to the end, start from the second element

|3*|2|1|5*|4|
|:-:|:-:|:-:|:-:|:-:|
|5*|2|1|3|4|
|5|2*|1|3*|4|
|5|3*|1|2|4*|
|5|4*|1|2|3|
|5|4|1*|2*|3|
|5|4|2*|1|3*|
|5|4|3*|1|2|
|5|4|3|2*|1|

## Pseudo code
>for itr1 = 0 to length(list)
>	for itr2 = itr + 1 to length(list)
>		if list[itr1] < list[itr2]
>			swap list[itr1], list[itr2]
>return list
- This program is organized with data structure and algorithm
	- data structure: list
	- algorithm: bubble sort
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
