# OOP tamoillari 4 turga bo'linadi
# 1. Meros olish
# 2. Encapsulation
# 3. Polimorfizm
# 4. Abstraction

# class Person:
#     name = "Ali"

#     def __init__(self, name = "Bobur"):
#         self.name = name


# class Toti(Person):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return f"{self.name} salom"


# obj = Toti("Bobur")
# print(obj.speak())

# Encapsulation
# class Car:

#     def __init__(self, color):
#         self.__color = color

#     def __car_color(self):
#         return f"Ferrarini rangi {self.__color}"

#     def open_car(self):
#         return self.__car_color()

# obj = Car("red")
# print(obj.open_car())

# class Classy:
#     def visible(self):
#         print("visible")
    
#     def __hidden(self):
#         print("hidden")
    
#     def open_function(self):
#         print(self.__hidden())

# obj = Classy()
# obj.visible()
# obj.open_function()
# try:
#     obj.__hidden()
# except:
#     print("bu funksiya blocklangan")

# Polimorfizm
# class Perot:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"Mening ismim {self.name}"

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Vov - vov"

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"Meow - meow"

# def connect():
#     print(Perot("Kesha").speak())
#     print(Dog("Bobik").speak())
#     print(Cat("Mosh").speak())

# connect()

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

shapes = [Circle(3), Rectangle(4, 5)]
for s in shapes:
    print(s.area())

