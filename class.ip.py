''' ClASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("========== INHERITENCE ========")
# Parent > CHILD


class Animal:  # Parent
    # state
    description = "The class creates animals"

    # constructor
    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("play")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)

dog.introduce()
cat.introduce()

print(dog.voice)
print("status", dog.status)
