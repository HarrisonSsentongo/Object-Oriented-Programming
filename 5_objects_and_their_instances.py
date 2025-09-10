class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking! Woof Woof!")

# Create object
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving...")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying in the sky!")

# Objects
animal = Animal("Generic Animal")
bird = Bird("Eagle")

animal.move()
bird.move()


class Cat:
    def sound(self):
        print("Meow Meow!")

class Dog:
    def sound(self):
        print("Woof Woof!")

# Polymorphism in action
animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Object
account = BankAccount(1000)
account.deposit(500)
print("Current balance:", account.get_balance())


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Object
circle = Circle(7)
print("Area of circle:", circle.area())
