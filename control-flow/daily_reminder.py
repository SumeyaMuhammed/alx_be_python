task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
  case "high":
    print(f"'Reminder: {task}' is a high priority task", end="")
    if time_bound == "yes":
      print(" that requires immediate attention today!")
    else:
      print(". Consider completing it when you have free time.")
  case "low":
    print(f"Note: '{task}' is a low priority task", end="")
    if time_bound == "yes":
      print(" that requires immediate attention today!")
    else:
      print(". Consider completing it when you have free time.")