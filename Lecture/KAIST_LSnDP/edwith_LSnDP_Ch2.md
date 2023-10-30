[EDWITH: Linear Structure and Dynamic Programming](https://www.edwith.org/datastructure-2019s)   
Chapter 2: Object Oriented Paradigm
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
```Python
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
# Reference Variables *self* and *super*
- From Python, *self* is...
	- Reference variable pointing the instance itself
- From Python, *super* is...
	- Reference variable pointing the base class instance
	- *super* is used to ca;l the base class methods
## Practice
```Python
'''
self: reference variable pointing the instance itself

super: reference variable pointing the base class instance
       super is used to call the base class methods.
'''
class Father(object):
    strHometown = "Jeju"
    def __init__(self, paramHome):
        self.strHometown = paramHome
        print("Father is created")
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHomeTown = "Seoul"
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")

class Child(Father, Mother):
    strName = "Moon"
    def __init__(self, paramName, paramHome): #when an instance is created, two arguments will be 'pramName', 'paramHome'
        super(Child, self).__init__(paramHome) #bring the 'paramHome' from the superclass 'Father'
        self.strName = paramName
        print("Child is created")
    def doRunning(self):
        print("Fast")

me = Child("Sun", "Universe") #Father is created, Child is created
me.doFatherThing() #Father's action
me.doMotherThing() #Mother's action
me.doRunning() #Fast
print(me.strHomeTown) #Universe
print(me.strName) #Sun
```
# Polymorphism
- Method Overriding & Overloading
- After get method from superclass, subclass can modify the method in two ways: overriding, overloading
- We can also set the default parameter value
## Method Overriding
- Base class has a method A(num),
  and its derived class has a method A(num)
## Method Overloading
- A class has a method A(num),
  A(num, name),
  and A(num, name, home)
## Practice
```python
'''
method overriding: change the behavior of existing methods

method overloading: more than one method of the same class shares the same method name having different signatures
'''
class Building:
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door Opened")

class Hotel(Building):
    def openDoor(self): #overriding of the method 'openDoor' from the super class 'Building'
        print("Bellboy opens a door")
    def checkIn(self, days = 1): #overloading by putting default value of the parameter
        print("Someone checks in for", days, "days")

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn() #default value of 'days' is 1. So in here, the method 'checkIn' looks like doesn't have any parameter.
lotteHotel.checkIn(2) #the method 'checkIn' gets parameter but still works with overloading.
```
# Abstract class (=Abstract Base Class)
- A class with an abstract method
	- The abstract method is a method with signature, but with no implementation
	- The abstract method is not a complete
	- You can't make an instance out of it
- By abstract class, we can design more carefully
	- The main purpose is inheriting the abstract method to subclass and let that override it
## Practice
```python
'''
abstract class: A class with an abstract method

abstract method: A method with signature, but with no implementation.
                 Abstract method is not a complete.
                 You can't make an instance out of it.
                 The concrete class with 'full' implementations and inheriting the abstract class will be a basic for instances.
'''
from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod #indicator of abstract base method and class
    def openDoor(self):
        pass
    @abstractmethod
    def openWindow(self):
        pass

class BedRoom(Room):
    def openDoor(self):
        print("Open bedroom door")
    def openWindow(self):
        print("Open bedroom winodw")

class Lobby(Room): #this class has a lack of method, 'openWindow' which is the abstract base method of the super calss.
    def openDoor(self):
        print("Open lobby door")

room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))

lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))
```
# *Object* class 
- The top superclass of all of classes
	- Or, think it as like default type of class
- Every Python classes are the descendeants of *Object*
	- When we code like `class name:` it's actually like `class name(object):`
- *Object* class has several methods
	- *init*
	- *del*
	- *eq*
	- *add*
	  ...
- We are actually override them to make the methods behave as we please
## Practice
```python
'''
All of Python classes are the descendants of Object.

Object class has many hidden methods: __init__  constructor
                                      __del__
                                      __eq__    T/F examination
                                      __cmp__   compare
                                      __add__   

We actually override to those hidden methods.
'''
class Room:
    numWidth = 100
    numHeight = 100
    numDepth = 100

    def __init__(self, parWidth, parHeight, parDepth): #actually overriding from the object class
        self.numDepth = parDepth
        self.numWidth = parWidth
        self.numHeight = parHeight
    
    def getVolume(self):
        return self.numDepth*self.numHeight*self.numWidth

    def __eq__(self, other):
        if isinstance(other, Room):
            if self.getVolume() == other.getVolume(): #Duck Typing: the variable is not defined yet
                return True
        return False
```