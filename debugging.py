'''Packages & Debugging
   (1) Python packages & Core Packages
   (2) Package Manager & External Packages
   (3) Debugging
'''

import turtle
print("========== Python packages & Core Packages ==========")
''' Python Packages/Modules: Core , File and  External Packages'''
# Core Packages > https://docs.python.org/3/library

# Core Packages
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
t.circle(150)

turtle.done()

print("==========")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)
print("DONE")
