FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return result

def convert_to_fahrenheit(celsius):
  result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return result

temprature =input("Enter the temperature to convert: ")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if type(temprature) != float:
  print("Invalid temperature. Please enter a numeric value.")
  exit()
if unit == "c":
  print(f"{temprature}°C is {convert_to_fahrenheit(temprature)}°F")
elif unit == "f":
  print(f"{temprature}°F is {convert_to_celsius(temprature)}°C ")
else:
  print("Invalid unit. Please enter a proper unit.")
