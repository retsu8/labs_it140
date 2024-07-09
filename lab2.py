import calendar
import sys
from datetime import datetime, date, timedelta


def date_range(start, end):
    return [start + timedelta(days=x) for x in range((end - start).days)]


input_month = input()
input_day = int(input())
now_year = datetime.today().year

months = {calendar.month_name[i]: i for i in range(1, 12)}
if input_month not in months.keys():
    print("Invalid")
    sys.exit()

# Quick generate an easy calendar with seasons.
# Put one date further to handle the range up to function.
yearly_calendar = {
    "Spring": date_range(date(now_year, 3, 20), date(now_year, 6, 21)),
    "Summer": date_range(date(now_year, 6, 21), date(now_year, 9, 22)),
    "Autumn": date_range(date(now_year, 9, 22), date(now_year, 12, 21)),
    "Winter": date_range(date(now_year, 12, 21), date(now_year, 12, 31))
    + date_range(date(now_year, 1, 1), date(now_year, 3, 20)),
}

try:
    season_date = date(now_year, months[input_month], input_day)
except ValueError as e:
    print("Invalid")
    sys.exit()

for season in yearly_calendar.keys():
    # This Will print the season.
    if season_date in yearly_calendar[season]:
        print(season)