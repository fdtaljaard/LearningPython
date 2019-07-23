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

	# create 'constructor' method - I like this
	@classmethod
	def new_location(cls, location_str):
		name, barcode, description = location_str.split('-')
		return cls(name, barcode, description)

# call class method site will be JHB until you change
Location.set_site('JHB')

# instance of class via __init__
l1 = Location('Loc1', 'LOC1', 'Location 1')

# instance of class via classmethod
l2 = Location.new_location('Loc2-LOC2-Location 2')
print(l2.name)

print(l1.site)
l1.site = 'CPT'

print(l1.site)

print(l1.fullName())

print(l1.__dict__)
