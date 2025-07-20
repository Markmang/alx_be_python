from unittest import case


task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
           reminder = "that requires immediate attention today!" 
           print(f"Reminder: '{task}' is a {priority} priority task {reminder}")
        else:
            reminder = "try to address it as soon as possible."
            print(f"Reminder: '{task}' is a {priority} priority task {reminder}")
    case "medium":
        if time_bound == "yes":
            reminder = "that should be completed today."
            print(f"Reminder: '{task}' is a {priority} priority task {reminder}")
        else:
            reminder = "Plan to do it this week."
            print(f"Reminder: '{task}' is a {priority} priority task {reminder}")
    case "low":
        if time_bound == "yes":
            reminder = "is a low priority task, but it's time-sensitive. Don't forget to finish it today!"
            print(f"Reminder: '{task}' is a {priority} priority task {reminder}")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority level. Please enter high, medium, or low.")
