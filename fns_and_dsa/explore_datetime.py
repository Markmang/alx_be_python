from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date
print("Current date and time:",display_current_datetime())

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date() :
    future_date = datetime.now() + timedelta(days=number_of_days)
    future_date = future_date.strftime("%Y-%m-%d")
    return future_date
print("Future date:", calculate_future_date())

