[EDWITH: Linear Structure and Dynamic Programming](www.edwith.org/datastructure-2019s)   
Chapter 4: Recursions and Dynamic Programming
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
# Dynamic Programming
- *Dynamic Programming* is a general algorithm **design technique**
  (It's not an algorithm as like *Recursion*)
  - *Dynamic Programming* is defined by or fomulated as recurrences with overlapping sub-instances
- Using a table, writing down the result of each instances in advance
- Setting up a recurrence
	1) Solve small instances once
	2) Record solutions in a table
	3) Extract a solution of a larger instance from the table
## Memoization
- One of optimization techniques for *Dynamic Programming*
- Sotring the results of previous function calls to reuse the results again in the future
### Differences between Recursion's StackFrame and Dynamic Programming's Memoization
- StackFram is top-down
	- F(1)
	- F(2) -> F(1)
	- F(3) -> F(2) -> F(1)
	- F(4) -> F(3) -> F(2) -> F(1)
- Memoizaiton is bottom-up 
	- F(1)
	- F(2) <- F(1)
	- F(3) <- F(2)
	- F(4) <- F(3)
## Practice
```python
'''
Dynamic programming(DP): DP is an algorithm 'design' technique.
                         It has recurrences with overlapping sub-instances.

Memoization: Memoization is one of the optimization techniques for DP.
             Simply storing the results of previouis function calls to reuse it later.

We can solve the Fibonacci problem again while using DP's memoization.
'''
def FibonacciDP(n):
    dicFibonacci = {} #using a dictionary collection variable type for memoization.
    dicFibonacci[0] = 0
    dicFibonacci[1] = 1

    for itr in range(2, n+1): #building up a bigger solutions
        dicFibonacci[itr] = dicFibonacci[itr-1] + dicFibonacci[itr-2]
    return dicFibonacci[n]


for itr in range(0, 10):
    print(FibonacciDP(itr), end=" ")

'''
compare with the recursion's Fibonacci solution in big-O,
    recursion spends O(2^n)
    DP spends O(N)
'''
```
# Solving Assembly Line Sceduling problem in Recursion and DynamicProgramming
[To understand concept -> Geeks for Geeks: Assembly Line Scheduling](https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/)
<img src="https://media.geeksforgeeks.org/wp-content/uploads/AssembleScheduling1.png">
## 1. Using Recursion
```python
'''
There are two assembly lines.
Each assemply line has six stations.
Each 12 stations have their own consuming time.
Also, each line has enter and exit belt, which also needs time to pass.
When you pass the one station, you have two options: 1) stay in the same assembly line and go to the next station
                                                     2) cross to another assembly line through the belt and go to the next station of the line
                                                        (when you cross, it needs another additional time)

'''
class AssemblyLines:
   timeStation = [[7, 9, 3, 4, 8, 4],
                  [8, 5, 6, 4, 5, 7]]
   timeBelt = [[2, 2, 3, 1, 3, 4, 3],
               [4, 2, 1, 2, 2, 1, 2]]
   intCount = 0

   def Scheduling(self, idxLine, idxStation):
      print("Calculate scheduling: line, station: ", idxLine, idxStation, "(", self.intCount, "recursion calls )")
      self.intCount = self.intCount + 1

      #escape when it's not for the recursion
      if idxStation == 0: 
         if idxLine == 1:
            return self.timeBelt[0][0] + self.timeStation[0][0]
         elif idxLine == 2:
            return self.timeBelt[1][0] + self.timeStation[1][0]

      #recursion
      if idxLine == 1:  
         costLine1 = self.Scheduling(1, idxStation-1) + self.timeStation[0][idxStation]
         costLine2 = self.Scheduling(2, idxStation-1) + self.timeStation[0][idxStation] + self.timeBelt[1][idxStation]
      if idxLine == 2:
         costLine1 = self.Scheduling(1, idxStation-1) + self.timeStation[1][idxStation] + self.timeBelt[0][idxStation]
         costLine2 = self.Scheduling(2, idxStation-1) + self.timeStation[1][idxStation]

      if costLine1 > costLine2:
         return costLine2
      else:
         return costLine1
      
   def startScheduling(self):
      numStation = len(self.timeStation[0])
      costLine1 = self.Scheduling(1, numStation - 1) + self.timeBelt[0][numStation]
      costLine2 = self.Scheduling(2, numStation - 1) + self.timeBelt[1][numStation]
      if costLine1 > costLine2:
         return costLine2
      else:
         return costLine1


lines = AssemblyLines()
time = lines.startScheduling() # 125 times calling
print("Fastest production time:", time) #38
```
## 2. Using Dynamic Programming
```python
'''
There are two assembly lines.
Each assemply line has six stations.
Each 12 stations have their own consuming time.
Also, each line has enter and exit belt, which also needs time to pass.
When you pass the one station, you have two options: 1) stay in the same assembly line and go to the next station
                                                     2) cross to another assembly line through the belt and go to the next station of the line
                                                        (when you cross, it needs another additional time)

'''
class AssemblyLines:
   timeStation = [[7, 9, 3, 4, 8, 4],
                  [8, 5, 6, 4, 5, 7]]
   timeBelt = [[2, 2, 3, 1, 3, 4, 3],
               [4, 2, 1, 2, 2, 1, 2]]
   
   #setting up a memoization table
   timeScheduling = [list(range(6)), list(range(6))] #consider it as an empty list
   stationTracing = [list(range(6)), list(range(6))] 

   def startSchedulingDP(self):
      #table initiation
      numStation = len(self.timeStation[0])
      self.timeScheduling[0][0] = self.timeStation[0][0] + self.timeBelt[0][0] 
      self.timeScheduling[1][0] = self.timeStation[1][0] + self.timeBelt[1][0] #Scheduling becomes [[9, _, _, _, _, _], [12, _, _, _, _, _]]

      #dynamic programming
      for itr in range(1, numStation):
         if self.timeScheduling[0][itr-1] > self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]:
            self.timeScheduling[0][itr] = self.timeScheduling[0][itr] + self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]
            self.stationTracing[0][itr] = 1
         else:
            self.timeScheduling[0][itr] = self.timeStation[0][itr] +  self.timeScheduling[0][itr-1]
            self.stationTracing[0][itr] = 0

         if self.timeScheduling[1][itr-1] > self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]:
            self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]
            self.stationTracing[1][itr] = 0
         else:
            self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[1][itr-1]
            self.stationTracing[1][itr] = 1
      
      #caculate the time cost overall
      costLine1 = self.timeScheduling[0][numStation-1] + self.timeBelt[0][numStation] #adding last belt's time
      costLine2 = self.timeScheduling[1][numStation-1] + self.timeBelt[1][numStation] #adding last belt's time
      
      #compare between two paths
      if costLine1 > costLine2:
         return costLine2, 1
      else:
         return costLine1, 0

   def printTracing(self, lineTracing):
      numStation = len(self.timeStation[0])
      print("Line: ", lineTracing,", Station:", numStation)
      for itr in range(numStation-1, 0, -1):
         lineTracing = self.stationTracing[lineTracing][itr]
         print("Line:", lineTracing, ", Station:", itr)


lines = AssemblyLines()
time, lineTracing = lines.startSchedulingDP() # 6 times calling
print("Fastest produiction time:", time) #38
lines.printTracing(lineTracing)
```
- Dynamic Programming calls only 6 times while Recursion calls 125 times