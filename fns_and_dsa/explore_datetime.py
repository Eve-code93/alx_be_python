from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print("Current date and time:", formatted_date)

def calculate_future_date():
    # Ask the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print("Future date:", formatted_future_date)

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

