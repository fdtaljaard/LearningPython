class Car():

	speed = 0
	def __init__(self, speed):
		self.speed = speed

c = Car(10)

# maybe not best example
c.accelerator = lambda self, x: print('speed ' + str(self.speed + x))

# not sure if you can do away with passing instance of object
c.accelerator(c, 60)