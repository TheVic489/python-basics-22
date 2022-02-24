from pathlib import Path
from datetime import date

# -----------------------------------------------------------------------------
# Student name: WRITE YOUR NAME HERE
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Q2: get_class_days()
# - Input:
#   - Start date:  int
#   - End date:    int (INCLUDED!)
#   - Holiday_txt: str. The holidays of December 2021.
# - Output:
#   - class_days: list[int] with all class days in December 2021 between
#                 start and end (included), excluding weekends and holidays.
# 
# - Recommended algorithm:
#   1. Create a list of dates with all days between start and end.
#   2. Create a list of dates with all holidays.
#   3. Create a new list with all dates that are not in the holidays list and are not a weekend.
#      - For holidays, use the 'in' boolean operator as follows:  1 in [1, 2, 3]
#      - For weekends, use the provided function get_weekday().
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - You can write additional functions to simplify your algorithm.
# -----------------------------------------------------------------------------


# - Returns the weekday, assuming it is a day of December 2021.
# - 1 = Monday, 2 = Tuesday, ... 7 = Sunday
# - Usage example: get_weekday(1) -> 3  # Wednesday
# -----------------------------------------------------------------------------
def get_weekday(day: int) -> int:

    return date.fromisoformat(f"2021-12-{day:02}").isoweekday()


# - Input:  Two days of December 2021 as ints
# - Output: A list of days (ints). Includes the end day!
# -----------------------------------------------------------------------------
def get_all_days(start: int, end: int) -> list[int]:

    all_days: list[int] = list(range(start, end+1))

    return all_days


# - Input:  The contents of the file "q2_holiday.txt" as a string.
# - Output: A list of days (int)
# -----------------------------------------------------------------------------
def get_holidays(holiday_txt: str) -> list[int]:

    holiday_str_list: list[str] = holiday_txt.split()
    holiday_int_list: list[int] = []

    for holiday_str in holiday_str_list:
        holiday_int: int = int(holiday_str)
        holiday_int_list.append(holiday_int)

    return holiday_int_list


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_class_days(start: int, end: int, holiday_txt: str) -> list[int]:

    all_days: list[int] = get_all_days(start, end)
    holidays: list[int] = get_holidays(holiday_txt)
   
    class_days: list[int] = []

    for day in all_days:

        weekday: int = get_weekday(day)

        is_weekend: bool = (weekday == 6) or (weekday == 7)
        is_holiday: bool = (day in holidays)

        if (not is_weekend) and (not is_holiday):
            class_days.append(day)

    return class_days


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Write your solution inside the function.
    # Code here is not evaluated.
    # This is just for your convenience.
    holiday_txt: str = Path("q2_holiday.txt").read_text()
    print(get_class_days(1, 15, holiday_txt))

# -----------------------------------------------------------------------------
