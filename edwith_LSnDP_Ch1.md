[EDWITH: Linear Structure and Dynamic Programming](https://www.edwith.org/datastructure-2019s)   
Chapter 1
# What Makes You As a Good Engineer?
- Programming is an implementation tool.
## Good engineer needs...
- Conceptual thinking and design
- Practical design and implementation
## To programmer, the design means 'algorithm design'
- We will learn UML to understand 'data structure' and 'algorithm design' -> first priority
- We will learn Python to implement the design -> second priority
	- If the design is bad, implementation is meaningless
- Of course, good programmers should be good at BOTH

# What is Python?
- Python is Interpreter language
	- Opposite to Compiled language
	- Compiled language cannot run an imperfect code
	- However, the Interpreter language code(Python) can run an imperfect code
- Python is Object-oriented language
- Python can dynamic type of variables.
	- The types of variables can be changed anytime 
	- This is opposite to Compiled language
- Python is fasy to develop but slow to execute
	- Meanwhile, Compiled language programming is slow to develop but fast to execute
- Python is specialized in data analyses

# Procedure-oriented vs Object-oriented
## What is Procedure-oriented Programming?
- Opposite to Object-oriented Programming
- Procedure-oriented Programming does not use Class
- Largely in two parts: 1) Definition part 2) Execution part
```Python
'''
This is 'Procedure-oriented' Hello World code.
Meaning, code has only functions.

'''

def main():    #function
    print ("Hello, world")
    print ("This program computes the average of two exam scores.")

    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    average = (int(score1) + int(score2)) / 2.0

    print("The average of the scores is: ", average)
main()
```

## What is Object-oriented Programming
- Object-oriented Programming use Class
- Largely in two parts: 1) Definition part 2) Execution part
```Python
'''
This is 'Object-oriented' Hello World.
Meaning, using class to make an instance later.

'''
class HelloWorld: #class name -> noun, camel casing
    def __init__(self): #constructor
        print ("Hello, world")

    def __del__(self):
        print ("Good Bye!")

    def performAverage(self, val1, val2): #method name -> verb, start with lower case
        average = (val1 + val2) / 2.0 #variable name -> noun, start with lower case
        print("The average of the scores is: ", average)

def main(): 
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    world.performAverage(int(score1), int(score2))

main()

'''
Also, check the naming and styling recommendations

For class,
    - Noun for the concept to eb represented by the class
    - Capitalize the first letter of each word

For variable,
    - Noun for the contents to be stored
    - Start with lower case
    - Not recommend to note the type of variable
      (variable's type can be changed easily from Python)

For method,
    - Verb for the method action
    - Start with lower case
'''
```

# Naming and Styling
**For Class**
-  Capitalize the first letter of each word
- e.g. MyFirstClass
**For Variable**
- Start with lower case
- Do not recommend to put the name of type front (Hungarian Notation style?)
- e.g. numberOfStudents = 100
**For Function, Method**
- Start with lower case
- Start with verb
- e.g. getNumber

# Operator
- Result of operation is displaced which has more information
- e.g. int(10)/int(3.0) = 3.333335

# Function Statement
- You can return multiple variables
	- But keep them in order
- You do not have to specify return types
```Python
def name(parameters):
	statements
	return variable1 variable2...
```
- One line function is called *lambda* function
```Python
lambda <parameters> : <return>
```

```Python
numA = 1
numB = 2

lambdaAdd = lambda numParam1, numParam2 : num Param1 + numParam2

numL = lambdaAdd(numA, numB)
print(numL)
```

# What is different between 'A is B' and 'A == B'?
- 'A is B' checks their objects' IDs
- 'A == B' checks their values
```Python
k=2
A=[1, 2, 3]
B=[1, k, 3]

# A is B -> False
# A == B -> True
```

# Class and Instance
- Class is like a blue print
- Instance is like a house, which is built based on the blue print, the Class
- One blue print -> Several Houses, but with slightly different features
```Python
class MyHome:
	colorRoof = 'red'
	stateDoor = 'closed'
	def paintRoof(self, color):
		self.colorRoof = color
	def openDoor(self):
		self.stateDoor = 'open'
	def closeDoor(self):
		self.stateDoor = 'close'
	def printStatus(self):
		print("Roof color is", self.colorRoof, ", and door is", self.stateDoor)


homeAtTokyo = MyHome() #instance
homeAtSeoul = MyHome() #instance

homeAtSeoul.openDoor()
homeAtTokyo.paintRoof('blue')

homeAtTokyo.printStatus()
homeAtSeoul.printStatus()
```

# Constructor, Destructor in Class
## Constructor
- Called when instantiated
## Destructor
- Called when the instance is removed from the value table
- Clearly removing the class
- Rarely used
Let's add the constructor and destructor on the above code.
```Python
from time import ctime   #Let's add time info

class MyHome:
	colorRoof = 'red'
	stateDoor = 'closed'
	def paintRoof(self, color):
		self.colorRoof = color
	def openDoor(self):
		self.stateDoor = 'open'
	def closeDoor(self):
		self.stateDoor = 'close'
	def printStatus(self):
		print("Roof color is", self.colorRoof, ", and door is", self.stateDoor)
	def __init__(self, strAddress):   #Constructor
		print("Built on", strAddress)
		print("Built at", ctime())
	def __del__(self):   #Destructor
		print("Destroyed at", ctime())


homeAtNewyork = MyHome('NYC')
homeAtNewyork.printStatus()
del homeAtNewyork
```

# Importing Module
- Write down Class codes in seperated files
- You can import them to anohter single code file
- Use from to specify the director, or the folder, path
- Let's say...
  1) Make *home.py* file which has Class, *HOME*
  2) Make *UsingMyHome.py* file, write down 'from *path* import HOME'
  3) Now you can use the class *HOME* in UsingMyHome.py file,

# Managing Modules by Package
- Several module files can be placed in one directory or folder
- We call these directories as **Package**
- Package folder should have *_init_.py* in the directory
  ```Python
  from <directory=package> import module
  ```
- When the module is placed in the same directory with the file which uses the module, we can skip to write *from*
  ```Python
  import module
  ```