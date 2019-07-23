class Location():

	site = ''

	def __init__(self, name, barcode, description):
		self.name = name
		self.barcode = barcode
		self.description = description

	# method for instance of class self
	def fullName(self):
		return self.name + '-' + self.description

	# method at class level cls (self not in scope)
	@classmethod
	def set_site(cls, site):
		cls.site = site

# call class method
Location.set_site('JHB')

# instance of class
l = Location('Loc1', 'LOC1', 'Location 1')

print(l.site)
l.site = 'CPT'

print(l.site)

print(l.fullName())

print(l.__dict__)
