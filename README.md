# Python Calendar Program

A simple console-based Python application that displays a selected
month's calendar and provides useful calendar information.

## Project Overview

The Python Calendar Program accepts a year and month from the user,
validates the input, displays the monthly calendar, and shows additional
information such as:

-   Month name
-   Number of days
-   First day of the month
-   Leap-year status

The project uses Python's built-in `calendar` module and exception
handling.

## Features

-   Accepts year and month from the user
-   Validates year and month values
-   Displays the selected monthly calendar
-   Shows the month name
-   Shows the number of days
-   Shows the first day of the month
-   Checks whether the year is a leap year
-   Handles invalid and non-numeric input safely

## Requirements

-   Python 3.x
-   No external libraries are required

## How to Run

1.  Make sure Python 3 is installed.
2.  Save the program as a Python file, for example
    `calendar_program.py`.
3.  Open a terminal or command prompt in the project folder.
4.  Run:

``` bash
python calendar_program.py
```

5.  Enter the requested year and month.

## Example

Input:

``` text
Enter year (e.g., 2026): 2026
Enter month (1-12): 9
```

The program displays the September 2026 calendar followed by calendar
information.

## Error Handling

The program handles:

-   Non-numeric input
-   Invalid or non-positive years
-   Months outside the range 1--12
-   Unexpected errors

## Main Python Functions Used

The program uses functions and data from Python's built-in `calendar`
module, including:

-   `calendar.month()`
-   `calendar.month_name`
-   `calendar.monthrange()`
-   `calendar.day_name`
-   `calendar.isleap()`

## Project Structure

``` text
Calendar Project/
├── calendar_program.py
└── README.md
```

## Future Enhancements

Possible improvements include:

-   Add a menu for viewing a full year
-   Allow repeated calendar searches without restarting
-   Add a graphical user interface
-   Add date/event notes and persistent storage
-   Export calendars to PDF or text files
-   Organize the application into multiple Python modules/classes

## Author

VITyarthi -- Build Your Own Project

## License

This project is created for educational purposes.
