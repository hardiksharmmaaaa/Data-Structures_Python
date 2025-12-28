## WAP That asks a user to input the day number in a year in the range of 2-365 and and asks the first day of the year (like Monday, Tuesday etc.) and then it should return the day on that particular day number.
day_number = int(input("Enter the day number in a year (2-365): "))
first_day = input("Enter the first day of the year (e.g., Monday, Tuesday): ")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 2 <= day_number <= 365:
    day_index = (day_number - 1) % 7
    print(f"The day on day number {day_number} is {days[day_index]}")
else:
    print("Invalid day number. Please enter a number between 2 and 365.")