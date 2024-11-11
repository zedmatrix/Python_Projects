from datetime import date
import calendar
import feedparser
today = date.today()
day = today.day
year = today.year

week_day = calendar.day_name[today.weekday()]  #Thursday
month = calendar.month_name[today.month]    #November

print(f'{today}')
print(f'Today is {week_day} ,{month} {day} {year}')
print("==================================")

match week_day:
    case "Sunday":
        print('Sunday Podcasts')

    case "Monday":
        print('Monday Podcasts')

    case "Tuesday":
        print('Tuesday Podcasts')

    case "Wednesday":
        print('Wednesday Podcasts')

    case "Thursday":
        print('Thursday Podcasts')

    case "Friday":
        print('Friday Podcasts')

    case "Saturday":
        print('Saturday Podcasts')

    case _:
        print('Unknown Week Day')

