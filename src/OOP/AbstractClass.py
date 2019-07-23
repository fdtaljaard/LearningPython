from abc import ABC, abstractmethod

# example based on abc lib
class AbstractBaseClass(ABC):
	
	@abstractmethod
	def DoYourThing(self):
		pass

class ConcreteClass(AbstractBaseClass):
	
	def __init__(self):
		pass
	
	def DoYourThing(self):
		print("ConcreteClass DoYourThing")

# kind of manual, could do this for interface class? 
class AbstractBaseClassManual():
	
	def DoYourThing(self):
		raise NotImplementedError

class ConcreteClassManual(AbstractBaseClassManual):
	
	def __init__(self):
		pass

c = ConcreteClass()
c.DoYourThing()

# Manual example
cM = ConcreteClassManual()
# raise error
cM.DoYourThing() 

# this not allowed because its an abstract class
# a = AbstractBaseClass()
# a.DoYourThing()