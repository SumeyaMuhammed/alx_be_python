# Exercise 1: Constructors and Destructors Instructions:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __del__(self):
    print(f"Person {self.name} has been deleted")

# Magic Methods (str and repr) Instructions:

class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Number of Pages: {self.pages}."
  
  def __repr__(self):
    return f"Book('{self.title}', '{self.author}', {self.pages})"
  
# Exercise 3: Class Inheritance Instructions:
class Animal:
  def eat(self):
    print(f"It eats!")

  def sleep(self):
    print(f"It sleeps")

class Dog(Animal):
  def bark(self):
    print("It sparks.")

animal = Animal()
animal.eat()
animal.sleep()
dog = Dog()
dog.sleep()
dog.bark()