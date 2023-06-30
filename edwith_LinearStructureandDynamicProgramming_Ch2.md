# Object-oriented paradigm(OOP)
## What is *object* from programming
- Class, Instance, inheritance, encapsulation, polymorphism ...
## What is Object-Oriented Design
- You have to program three things of object
	1) object's name
	2) object's features
	3) object's action
- Think about concept, not code.
	- Let's abstract the real world concepts into object design.
	- How can we abstract the information of customer from online banking?
		1) Customer's name
		2) Customer's featuer: bank ID, account number, ...
		3) Customer's action: login, request withdrawl, confirm security code, ...
## Class and Instance in Object-Orieted Design
- Right above, we designed 'Customer's basic concept'
- If we register foure different people as custoemers, each of them would register different names, bank IDs, requests, etc...
- Default customer information which is required -> *Class*
- Four customers' information following default form -> *Instance*
### Class
- Result of design and implementation
### Instance
- Result of execution
# The importance fo UML
- UML(Unified Modeling Language)
- Standarad design for software engineering
- Learning standard from field is important to communicate with your team
# Encapsulation
- Utilizing the visibility of your object
- Object = Data + Behavior
	- Behavior: method, member function, operation
- Types of visibility
	- Private: seen only within the class
	- Protected: seen only within the class and its descendants
	- Public: seen everywhere
- Recommended policy is like...
	- Data -> private
	- Behavior -> public
- Python cannot restrict t he visibility
	- One promise between developers is that if the file name has two underscores before the name( _ _ example.py), **do not touch**
# Inheritance between *Class*
- Giving attributes to descendants
	- Attributes are including member variables, methods
- Descendants will get attributes but...
	- Descendants can have their own attributes
	- Descendants can overlap the attributes they got
- JAVA's class can have only one parent
- Python's class can have several parents
## Superclass
- Ancestor, parents
- In design, generalized class
## Subclass
- Descendants
- In design, specialized class
## Practice
- In Python, to be inherited...
	- Write down the Superclass's name as a parameter
```
'''
inheritance: Giving my attribute(member variables, methods) to my descendants

superclass: my ancestors, specifically my father
            Python let the class has more than two one parent class(<-> Java)

subclass: my descendatns, specifically my son
'''

class Father(object): #the superest class is inherited from 'object' class
    strHomeTown = "Jeju"
    def __init__(self): #constructor
        print("Father is created")
    def doFatherThing(self): #method
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHomeTown = "Seoul"
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother): #the class 'Child' has two super classes
    strName = "Moon"
    def __init__(self):
        super(Child, self).__init__() #call the super class 'Father'
        print("Child is created")
    def doRunning(self): #method override
        print("Fast")

me = Child() #instance created
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHomeTown)
print(me.strName)
```
- SuperClass1: strHometown, doFatherthing(), doRunning()
- SuperClass2: strHometown, doMotherthing()
- SubClass: strName, doRunning()
	- SubClass's doRunning() method will be ovelapped