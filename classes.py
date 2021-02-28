Classes

__init__ method constructor
self refering to itself to re-use the vars .etc..


getters and setters methods
- access and use object data

property is like an property

decorators establish properties of some object
@color.setter
def color(self, color):
   self._color = color
    
@property
def title(self):
    return self.Tittle
  
  
Classmethod  - can be called without instancing the class
classrabbit:
  location = 'dasd'
  def __init__(self,weapon):
    self.weapon = weapon
  def display(self):
    print(weapong)
  @classemethod
  def get_location(cls)
    return cls.location
  
  
Inheritance.
- baseclass
- super
- multiple inheritance 
  - last classes added override -> mro shows the resolution order
  
 Abstracted classes
  - abcmeta, abastramethod
  
 Stratic methods
- doesn't need data from the calass
https://www.freecodecamp.org/news/python-property-decorator/
  
  
  class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price
  
