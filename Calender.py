import calendar

print("=" * 40)
print("       CALENDAR PROGRAM")
print("=" * 40)

try:
    year = int(input("Enter year (e.g., 2026): "))
    month = int(input("Enter month (1-12): "))

    if year <= 0:
        print("Error: Enter a valid year.")

    elif month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")

    else:
        print("\n" + calendar.month(year, month))

        print("Calendar Information")
        print("-" * 30)

        print("Year:", year)
        print("Month:", calendar.month_name[month])

        days = calendar.monthrange(year, month)[1]
        print("Number of days:", days)

        first_day = calendar.monthrange(year, month)[0]
        print("First day:", calendar.day_name[first_day])

        if calendar.isleap(year):
            print("Leap Year: Yes")
        else:
            print("Leap Year: No")

        print("-" * 30)
        print("Program completed successfully!")

except ValueError:
    print("Error: Please enter numbers only.")

except Exception as e:
    print("Error:", e)