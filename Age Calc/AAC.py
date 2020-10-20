
print("#" * 50, end = "")
print(
"""
#    Date And Time Units:                        #
#    1. enter months or m for month's unit       #
#    2. enter weeks or w for week's unit         #
#    3. enter days or d for day's unit           #
#    4. enter hours or h for hour's unit         #
#    5. enter minutes or min for minute's unit   #
#    6. enter seconds or s for second's unit     #
""", end = "")
print("#" * 50,)
# Collect Age Data
age = int(input("\nPlease Enter Your Age --> ").strip())

# Collect Date and Time Unit Data
unit = input("\nPlease Choose Unit --> ").strip().lower()

# Get age in all time units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if unit == "months" or unit == "m":
    print("\nYou choosed the unit month's")
    print(f"You lived for {months:,d} month's")

elif unit == "weeks" or unit == "w":
    print("\nYou choosed the unit week's")
    print(f"You lived for {weeks:,d} week's")

elif unit == "days" or unit == "d":
    print("\nYou choosed the unit day's")
    print(f"You lived for {days:,d} day's")

elif unit == "hours" or unit == "h":
    print("\nYou choosed the unit hour's")
    print(f"You lived for {hours:,d} hour's")

elif unit == "minutes" or unit == "min":
    print("\nYou choosed the unit minute's")
    print(f"You lived for {minutes:,d} minute's")

elif unit == "seconds" or unit == "s":
    print("\nYou choosed the unit second's")
    print(f"You lived for {seconds:,d} second's")
