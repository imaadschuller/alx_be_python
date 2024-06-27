# Prompt the user for task details
Task = input("Enter the task description: ")
Priority = input("Enter the priority level (high, medium, low): ").lower()
Time_Bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f"High priority task: {task}"
    case 'medium':
        reminder = f"Medium priority task: {task}"
    case 'low':
        reminder = f"Low priority task: {task}"

    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"

# Provide a customized reminder
print(reminder)

