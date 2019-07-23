from abc import ABC, abstractmethod

class AbstractBaseClass(ABC):
	
	@abstractmethod
	def DoYourThing(self):
		pass

class ConcreteClass(AbstractBaseClass):
	
	def __init__(self):
		pass
	
	def DoYourThing(self):
		print("ConcreteClass DoYourThing")

c = ConcreteClass()
c.DoYourThing()

print(dir(c))