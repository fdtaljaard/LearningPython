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
	
	# property / attribute , adding just to play and toy with
	prop = ''

	def __init_subclass__(self):
		print("BaseClass1 __init_subclass__")

	# constructor with param 
	def __init__(self, something):
		# set property
		self.prop = something
		print("BaseClass1 __init__ " + something)

	def Method1(self):
		print("BaseClass1 Method1 called")

	def Method2(self):
		print("BaseClass1 Method2 called")

# can inherint more than one class, take note it will 
# only call the first class __init_subclass__ ? 
class DerivedClass(BaseClass1, BaseClass):
	
	# never called?
	def __init_subclass__(self):
		print("DerivedClass __init_subclass__")

	# need to specify something else fails, wont pass to BaseClass1 have to call __init__
	def __init__(self, something):
		# constructor of BaseClass1 
		BaseClass1.__init__(self, something)
		print("DerivedClass __init__")

	def Method1(self):
		# override 
		print("DerivedClass Method1 called")

	def Method2(self):
		BaseClass.Method2(self)
		BaseClass1.Method2(self)
		print("DerivedClass Method2 called")


dc = DerivedClass('new')
# call DerivedClass Method3, inherit from BaseClass
dc.Method3()

# call DerivedClass Method1, almost like override
dc.Method1()

# call DerivedClass Method2
dc.Method2()

# property set via constructor 
print(dc.prop)
# is the instance of class ?type TypeOf?
print(isinstance(dc, BaseClass))
print(isinstance(dc, BaseClass1))
print(dir(dc))