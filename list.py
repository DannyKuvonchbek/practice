''' List
    (1) Working with list 
    (2) List methods
    (3) Lambda functions
    (4) enumerate, map and filter
'''
print("========== Working with list ==========")
# Java/PHP/NodeJs array => Python list

# literal
person = {"name": "Justin", "age": 25, }  # dictionary
people = ("Justin", "Martin", "Danny")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")

# constructor
letters = list("MIT!")
print(f"the letters: {letters} ands size: {len(letters)}")

print("==========")
fruits = ["apple", "banana", "orange", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0,2)
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("========== List methods ==========")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append letters: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")

print("==========")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("==============")
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable > sorted function & index() method
numbs = [2, 20, 12, 300]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("========== Lambda functions ==========")
# lambda is small anonymous function!
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("DANNY", 29),
    ("Michael", 30),
    ("Ali", 40),
]
people.sort()
print("people(1)", people)

# sort by age via lambda

people.sort(key=lambda person: person[1])
print("people(2)", people)

print("========== enumerate, map and filter ==========")
# enumerate for index & value
animals = ["dog", "cat", "capybara", "fish", "lion"]
for element in enumerate(animals):
    print("element:", element)

print("==========")
for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

print("==========")
# similar in dictionary
car_obj = dict(brand="BMW", model="seria 5", year=2020)    # dictionary
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} and value: {value}")

print("==========")
# map
cars = [
    ("BMW", 109),
    ("Tayota", 87),
    ("Audi", 116),
    ("Pagani", 33),
    ("Ferrari", 78)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_car(1):", new_cars)

result_map = map(lambda car: car[0], cars)
new_cars = list(result_map)
print("new_car(2):", new_cars)

print("==========")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result _filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
