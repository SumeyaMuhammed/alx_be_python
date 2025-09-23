#Practice Exercise

"""Exercise 1: Create a list to store names of your favorite fruits. Write code to access the second element and print it."""

Favorite_Fruits = ["apple", "orange", "watermelon"]
print(Favorite_Fruits[1])

"""Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre."""

Favorite_Book = {"Title": "Atomic Habits", "Author": "James Clear", "Genre": "Self-help"}

print(Favorite_Book["Genre"])

"""Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
"""

import random
numbers = []
for i in range(10):
  numbers.append(random.randint(1, 10))

unique_set = set(numbers)
print(unique_set)

