# daily_reminder.py

def daily_reminder():
    # Prompt for a Single Task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the Task Based on Priority and Time Sensitivity
    match priority:
        case 'high':
            reminder_message = f"Reminder: '{task}' is a high priority task"
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". You can complete it later."
                
        case 'medium':
            reminder_message = f"Reminder: '{task}' is a medium priority task"
            if time_bound == 'yes':
                reminder_message += " that requires attention soon!"
            else:
                reminder_message += ". Plan to do it when you can."
                
        case 'low':
            reminder_message = f"Reminder: '{task}' is a low priority task"
            if time_bound == 'yes':
                reminder_message += " but should be addressed today."
            else:
                reminder_message += ". Consider completing it when you have free time."
                
        case _:
            reminder_message = "Invalid priority level entered."

    # Provide a Customized Reminder
    print(reminder_message)

if __name__ == "__main__":
    daily_reminder()