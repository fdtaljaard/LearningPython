class BaseClass():
	
	def __init_subclass__(self):
		print("BaseClass __init_subclass__")

	def __init__(self):
		print("BaseClass __init__")

	def Method1(self):
		print("BaseClass Method1 called")

	def Method2(self):
		print("BaseClass Method2 called")

	def Method3(self):
		# override 
		print("BaseClass Method3 called")

class BaseClass1():
	
	def __init_subclass__(self):
		print("BaseClass1 __init_subclass__")

	def __init__(self):
		print("BaseClass1 __init__")

	def Method1(self):
		print("BaseClass1 Method1 called")

	def Method2(self):
		print("BaseClass1 Method2 called")

# can inherint more than one class, take note it will 
# only call the first class __init_subclass__ ? 
class DerivedClass(BaseClass1, BaseClass):
	
	def __init_subclass__(self):
		print("DerivedClass __init_subclass__")

	def __init__(self):
		# if you want to run base __init__
		super().__init__() 
		print("DerivedClass __init__")

	def Method1(self):
		# override 
		print("DerivedClass Method1 called")

	def Method2(self):
		BaseClass.Method2(self)
		BaseClass1.Method2(self)
		print("DerivedClass Method2 called")


dc = DerivedClass()
# call DerivedClass Method3, inherit from BaseClass
dc.Method3()

# call DerivedClass Method1, almost like override
dc.Method1()

# call DerivedClass Method2
dc.Method2()
# is the instance of class ?type TypeOf?
print(isinstance(dc, BaseClass))
print(isinstance(dc, BaseClass1))
print(dir(dc))