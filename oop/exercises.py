# Exercise 1: Single Inheritance Instruction:
class Shape:
  def calculate_area(self, area):
    return area
  
class Rectangle(Shape):
  def __init__(self, len, wid):
    self.length = len
    self.width = wid
  def calculate_area(self):
    return self.length * self.width


# Exercise 2: Multiple Inheritance Instruction:

class Bird:
  def fly(self):
    return "It flies!"
  
class Mammal:
  def run(self):
    return "It runs!"

class Bat(Bird, Mammal):
  def fly(self):
    return "It flies!"
  
  def run(self):
    return "It sometimes runs!"


# Exercise 3: Polymorphism with Duck Typing Instruction:

class Dog:
  def make_sound(self):
    return "Woof!"
  
class Cat:
  def make_sound(self):
    return "Meow!"
  
class Bird:
  def make_sound(self):
    return "Chirp!"
  
def let_them_speak(animals):
  for animal in animals:
    print(animal.make_sound())

sample_animals = [Cat(), Dog(), Bird()]    

let_them_speak(sample_animals)

