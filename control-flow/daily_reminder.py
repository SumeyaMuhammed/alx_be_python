task = input("Enter your task: ")
priority = input("input Priority (high/medium/low): ")
time_bound = input(" Is it time-bound? (yes/no): ")

match priority:
  case "high":
    print(f"'{task}' is a high priority task", end="")
    if time_bound == "yes":
      print(" that requires immediate attention today!")
    else:
      print(". Consider completing it when you have free time.")
  case "low":
    print(f"'{task}' is a low priority task", end="")
    if time_bound == "yes":
      print(" that requires immediate attention today!")
    else:
      print(". Consider completing it when you have free time.")