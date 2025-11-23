from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    Saves the current date in a variable named current_date.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    """
    Calculate and print the future date after adding the given number of days.
    Saves the result in a variable named future_date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    display_current_datetime()

    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
