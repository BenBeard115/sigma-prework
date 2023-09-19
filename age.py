from datetime import date
today = str(date.today())
present_year = int(today[0:4])
present_month = int(today[5:7])
present_day = int(today[8:10])

user_date = input("Enter a date in the form DD-MM-YYYY:")
user_day = int(user_date[0:2])
user_month = int(user_date[3:5])
user_year = int(user_date[6:10])


year_diff = present_year - user_year
month_diff = present_month - user_month
day_diff = present_day - user_day

if month_diff < 0 or month_diff == 0 and day_diff < 0:
    year_diff = year_diff - 1

print(year_diff)
