# daily_reminder.py

# daily_reminder.py

def daily_reminder():
    # Prompt for a Single Task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the Task Based on Priority and Time Sensitivity
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. You can complete it later.")
                
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a medium priority task that requires attention soon!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to do it when you can.")
                
        case 'low':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a low priority task but should be addressed today.")
            else:
                print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
                
        case _:
            print("Invalid priority level entered.")

if __name__ == "__main__":
    daily_reminder()