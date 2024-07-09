import calendar
import sys
from datetime import datetime, date, timedelta

# Set defaults for years
now_year = datetime.today().year
end_of_the_year = date(now_year, 12, 31)
begining_of_the_year = date(now_year, 1, 1)


def date_range(start, end):
    """Build Date range for season"""
    return [start + timedelta(days=x) for x in range((end - start).days)]


# Create month ranges from calendar module
months = {calendar.month_name[i]: i for i in range(1, 12)}

# Quick generate an easy calendar with seasons.
# Put one date further to handle the range up to function.
yearly_calendar = {
    "Spring": date_range(date(now_year, 3, 20), date(now_year, 6, 21)),
    "Summer": date_range(date(now_year, 6, 21), date(now_year, 9, 22)),
    "Autumn": date_range(date(now_year, 9, 22), date(now_year, 12, 21)),
    "Winter": date_range(date(now_year, 12, 21), end_of_the_year)
    + date_range(begining_of_the_year, date(now_year, 3, 20)),
}

# Ask for input for month, capitalized, and day.
input_month = input()
input_day = int(input())

# Check to make sure the month is valid
if input_month not in months.keys():
    print("Invalid")
    sys.exit()


# Test to make sure input is a valid date
try:
    season_date = date(now_year, months[input_month], input_day)
except ValueError as e:
    print("Invalid")
    sys.exit()

for season in yearly_calendar.keys():
    # This Will print the season.
    if season_date in yearly_calendar[season]:
        print(season)
