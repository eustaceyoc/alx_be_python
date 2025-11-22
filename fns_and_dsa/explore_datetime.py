from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

def calculate_future_date():
    days_to_add = (int(input("Enter the number of days to add to the current date:")))
    future_date = datetime.now() + timedelta(days=days_to_add)
    future_date = future_date.strftime("%Y-%m-%d")
    print(future_date)

display_current_datetime()
calculate_future_date()