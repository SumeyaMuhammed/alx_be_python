# Exercise 1: Class Methods for Counting Instances Instruction:

class Book:

  total_books = 0
  def __init__(self, title):
    self.new_book = title
    Book.total_books += 1
  @classmethod
  def display_total_books(cls):
    print(f"Total books created: {cls.total_books}")


# Exercise 2: Static Method for Utility Calculation Instruction:

class Calculator:

  @staticmethod
  def add(num1, num2):
    return num1 + num2
  
  @staticmethod
  def multiply(num1, num2):
    return num1 * num2
  
# Exercise 3: Class Method for Factory Creation Instruction:

class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def create_child(cls, name = "new_child"):
    return cls(name, 0)