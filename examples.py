## Pythonic Training
## Data Types

# to read 
# https://betterprogramming.pub/lambda-map-and-filter-in-python-4935f248593?gi=a149f1aed5b

List    [1,2,2,3,4,5,2]
Tuple  (2, ”dsad2”, ”2das”) |||   “borec”,
Dict   {“name”: “jeremey”, “age” : “20”}

# Being Phytonic - PEP 20
import this


**Unpicking variables**

birthday = (“hola”, “que”, 1)
Month, year, das = birthday

Listtuple = [ (2, ”dsad2”, ”2das”),(2, ”dsad2”, ”2das”),(2, ”dsad2”, ”2das”)]

For number, name, apple  in list_tuple:
	print

**Unpicking in functions:**

People =  [ (2, ”dsad2”, ”2das”),(2, ”dsad2”, ”2das”),(2, ”dsad2”, ”2das”)]

Def person_record(name, Merida, etst):
	print(name merada tests)

# use asterisk for tuples or list
# use 2 asterisk for dicts.
For person in people:
	person_record(*person)


**Sorting:**

Def bylenghtandname (item):
	return(len(item),item.lower())

Sorted = sort(people, key=bylenghtandname)



Lambda Function

addfive = lamba x : x +5
addfive(10)
Addtwonums = lamba x,y : x + y
Printnumber = lambda func, value :  print(func(value))
printnuber(additive, 5)


#CODE1: Use Lambda and Map to double numbers in a list
numbers = [1, 4, 6, 7, 9, 1, 43, 2, 2]
doubledMap = map(lambda x : x*2, numbers)
print(list(doubledMap))

#CODE2: Use Lambda and Filter to split list of numbers into odds and evens
numbers = [0, 24, 3, 7, 5, 2, 634, 26, 8, 33, 333, 100]
odds = filter(lambda x : x % 2 != 0, numbers)
evens = filter(lambda x : x % 2 == 0, numbers)
print(list(odds))
print(list(evens))

Lambdas are fine but far cleaner using list comprehension.

# list from range 0 to 10 
list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(list_) 
   
# lambda function 
lambda_list = list(map(lambda x: x * 2, list_)) 
  
# Map basically iterates every element 
# in the list_ and returns the lambda  
# function result 
print(lambda_list) 
   
# list comprehension 
list_comp = [x * 2 for x in list_] 
print(list_comp) 



List Comprehension

>>> numbers = [x**2 for x in numbers]
>>> numbers
[1, 4, 9, 16, 25]

#CODE1: Create a list with various elements and then define a list comprehension that filters on it
randomChars = ['a', 0, -3, 10, 4, 'p', '>', 7]
squaresList = [ x**2 for x in randomChars if type(x) == int ]
print(squaresList)

#CODE2: Create a list with various animal names and then define a set comprehension that filters on it
animalsList = [ 'whale', 'TIGER', 'lion', 'lion', 'X', 'ELEPHANT', 'cheetah', 'cat', 'DOG', 'W' ]
animalsSet = { animal[0].upper() + animal[1:].lower() for animal in animalsList if len(animal) > 1 }
print(animalsSet)


Dictionary Comprehension
>>> sorted_fruits
['Aaaa', 'bb', 'dos', 'mierda']
>>> comprehension = {a.lower() : len(a) for a in sorted_fruits}
{'aaaa': 4, 'bb': 2, 'dos': 3, 'mierda': 6}

#CODE3: Create a dict of square roots and then iterate of the items printing out each key-value pair
squareRoots = {x : x**0.5 for x in range(1,20)}
for idx, squareRoot in squareRoots.items():
  print(f'{idx}->{squareRoot:.3f}')


Set Comprehension
Sets ->  Unique values

with open('cancion') as torrada:
	 s = {w.lower() for i in torrada for w in re.split('\W+', i) if w}
Set -> {}


**generators** 
Generator Expression-  https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
Yield 
memory efficient.
Maintain state between calls



Functions, modules and packages
* In a function = no positional arguments
 - If __name__ == “__main__”: -> check whether program is the first executed.
 	do 

Packages - folder containing modules
Subpackages
__init__.py will run when importing	


Docstrings
