''' Comprehension
    (1) What is comprehension & list comp.
    (2) set and dictionary comp.
'''

print("========== What is comprehension & list comp. ==========")
# Comprehension acts like spread operator!

''' Comprehension general
    a) * iterable 
    b) <expression> for item in <iterable  
    c) <expression> for item in iterable <condition>
'''
# list comp.
numbers = [1, 2, 4, 2, 1, 20, ]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("===========")
people = [("Martin", 35), ("Danny", 29), ("Sophie", 19)]
list_people = [people[0] for person in people]  # b version
print("list_people:", list_people)

print("============")
cars = [
    ("BMW", 109),
    ("Tayota", 87),
    ("Audi", 116),
    ("Pagani", 33),
    ("Ferrari", 78)
]
list_cars = [car[0] for car in cars if car]  # c version
print("list_cars:", list_cars)

print("========== set and dictionary comprehension ==========")
numbs = [1, 2, 4, 2, 1, 20, 1, 4, 5, 4, 5]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

dic_people = {person[0]: person[1] for person in people}  # b version
print("dic_people:", dic_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # c version
print("dict_people2:", dict_people2)
