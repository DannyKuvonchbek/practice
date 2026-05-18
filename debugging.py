'''Packages & Debugging
   (1) Python packages & Core Packages
   (2) Package Manager & External Packages
   (3) Debugging
'''
from PIL import Image
import turtle
print("========== Python packages & Core Packages ==========")
''' Python Packages/Modules: Core , File and  External Packages'''
# Core Packages > https://docs.python.org/3/library

# Core Packages
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)

# turtle.done()

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

print("========== Package Manager & External Packages ==========")
''' Package Manager:
    Python pip pipenv
    NodeJs > npm yarn
    Php > composer 
    MacOS > brew
'''
# External Packages > https://pypi.org/
with Image.open("material/person.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")

print("========== Debugging ==========")


def get_summary(*args):  # Define
    total_amount = 0
    for a in args:
        total_amount += a
    return total_amount


test = 100
result = get_summary(1, 2, 3, 4, 5)  # Call
print("result:", result)
