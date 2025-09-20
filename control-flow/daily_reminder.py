task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
  case "high":
    if time_bound.lower() == "yes":
      print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
      print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
  case "medium":
    if time_bound.lower() == "yes":
      print(f"Reminder: '{task}' is a medium priority task that you should finish today.")
    else:
      print(f"Reminder: '{task}' is a medium priority task. Plan to work on it soon.")
  case "low":
    if time_bound.lower() == "yes":
      print(f"Reminder: '{task}' is a low priority task, but since it's time-bound, complete it today.")
    else:
      print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
  case _:
    print("Invalid priority entered. Please choose high, medium, or low.")