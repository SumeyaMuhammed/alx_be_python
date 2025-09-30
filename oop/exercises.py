class Student:
  def __init__(self, name, age ):
    self.name = name
    self.age = age

  def display(self):
    print(f"{self.name} is {self.age} years old.")

class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity =  quantity

  def total(self):
    total = self.quantity * self.price
    return total

p = Product("Notebook", 5.0, 10)
print(p.total())  # 50.0
