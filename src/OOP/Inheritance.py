class BaseClass():
	
	def __init_subclass__(self):
		print("BaseClass __init_subclass__")

	def __init__(self):
		print("BaseClass __init__")

	def BaseMethod():
		print("BaseClass method called")

class DerivedClass(BaseClass):
	
	def __init_subclass__(self):
		print("DerivedClass __init_subclass__")

	def __init__(self):
		super().__init__()
		print("DerivedClass __init__")

	def BaseMethod(self):
		BaseClass.BaseMethod()
		print("DerivedClass method called")


dc = DerivedClass()
dc.BaseMethod()