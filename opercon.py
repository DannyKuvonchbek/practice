''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("========== Operators =========")
# + - > >= < <= * / // % += **

a = 19
b = 5

print("a > b", a > b)
print("a * b", a * b)
print("a / b", a / b)

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b*b", b**2)
print("b**3", b**3)

print("="*5)

c = dict(name="Danny", age=29)
d = dict(name="Danny", age=29)
e = c

print("c==d", c == d)
print(id(c), id(d), id(e))

print("c is d", c is d)
print("c is e", c is e)

print("========== Condition =========")

x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


age = 20
# person = None
# if age > 16:
#    person = "adult"
# else:
#    person = "child"

# Ternary
person = "adult" if age > 18 else "minor"
print("person", person)

print("============")

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here , do you want to be student!")
elif is_admin:
    print("Please go to this office!")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
