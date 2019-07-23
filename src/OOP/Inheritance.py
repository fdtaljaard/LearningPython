class BaseClass():
	
	def __init_subclass__(self):
		print("BaseClass __init_subclass__")

	def __init__(self):
		print("BaseClass __init__")

	def BaseMethod():
		print("BaseClass method called")

class BaseClass1():
	
	def __init_subclass__(self):
		print("BaseClass1 __init_subclass__")

	def __init__(self):
		print("BaseClass1 __init__")

	def BaseMethod():
		print("BaseClass1 method called")
		
# can inherint more than one class, take note it will 
# only call the first class __init_subclass__ ? 
class DerivedClass(BaseClass1, BaseClass):
	
	def __init_subclass__(self):
		print("DerivedClass __init_subclass__")

	def __init__(self):
		# if you want to run base __init__
		super().__init__() 
		print("DerivedClass __init__")

	def BaseMethod(self):
		# if you want to call base BaseMethod
		BaseClass.BaseMethod()
		print("DerivedClass method called")


dc = DerivedClass()
dc.BaseMethod()