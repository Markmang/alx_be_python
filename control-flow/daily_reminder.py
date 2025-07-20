task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while True:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"\nReminder: '{task}' is a high priority task. Try to address it as soon as possible.")
            break
        case "medium":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"\nReminder: '{task}' is a medium priority task. Plan to do it this week.")
            break
        case "low":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a low priority task, but it's time-sensitive. Don't forget to finish it today!")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
            break
        case _:
            print("\nInvalid priority level. Please enter high, medium, or low.")
            priority = input("Priority (high/medium/low): ").lower()
