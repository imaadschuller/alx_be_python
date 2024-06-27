# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_Bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity

if priority == 'high':
    reminder = f"High priority task: {task}"
elif priority == 'medium':
    reminder = f"Medium priority task: {task}"
elif priority == 'low':
    reminder = f"Low priority task: {task}"
else:
    reminder = f"Unknown priority task: {task}"

    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"

# Provide a customized reminder
print(f"Reminder: {reminder}")

