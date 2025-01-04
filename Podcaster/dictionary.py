"""
    My Date Dictionary Function
        test: print(f"{Create_Dictionary()}")
"""

from datetime import date
import calendar

def Create_Dictionary():
    today = date.today()
    myDay = today.day
    myMonth = today.month
    myYear = today.year

    my_dict = {}

    my_dict["day"] = myDay
    my_dict["month"] = myMonth
    my_dict["year"] = myYear

    month = calendar.month_name[myMonth]            # January
    weekday = calendar.day_name[today.weekday()]    # Friday

    my_dict["fulldate"] = f"{weekday} {month}, {myDay}, {myYear}"

    month = calendar.month_abbr[myMonth]            # Jan
    weekday = calendar.day_abbr[today.weekday()]    # Fri
    my_dict["outdir"] = f"{month}_{weekday}_{myMonth:02d}-{myDay:02d}-{myYear}"

    return my_dict
