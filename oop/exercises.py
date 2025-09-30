# Exercise 1: Handling ZeroDivisionError

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
  print(num1 / num2)
except ZeroDivisionError :
  print("cannot devide by 0")

# Exercise 2: File Handling with FileNotFoundError

input_file = input("enter the file name: ")
try:
  with open(input_file) as f:
    for line in f:
        print(line, end="")
except FileNotFoundError:
  print("file doesn't exist")

# Exercise 3: Custom Exception

class ValueTooHighError(Exception):
  pass
input_number = float(input("Enter a number: "))
try:
  if(input_number > 100):
    raise ValueTooHighError("The number is too high.")
except ValueTooHighError as e:
  print(e)
