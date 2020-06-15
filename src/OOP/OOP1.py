import json 

class Car():
	def __init__(self,brand,model,year,km,color):
		self.brand = brand
		self.model = model
		self.year  = year
		self.km    = km
		self.color = color

	def create(self):
		new_car = {
			'brand': self.brand,
			'model': self.model,
			'year' : self.year,
			'km'   : self.km,
			'color': self.color
		}

		car = json.dumps(new_car)

		path = './cars.json'
		cars_file = open(path,'w')
		cars_file.write(car)
		cars_file.close()

class InheritanceCar(Car):
    
	def produce_car(self):
		return 'car produced at {} factory'.format(self.brand)

a = Car('vw','amarok','2020','0','grey')
a.create()
