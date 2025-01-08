"""
    Budget Data Constants, Table Headers

"""
from LibreOffice.color_data import *

# Header Constants
months = [ "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December" ]

column_headers = ["Budget", "Actual", "Difference"]
# Budget Summary
budget_summary = {"title": ["Monthly Budget Summary", {"fore_color": white, "back_color": dark_grey}],
                  "headers": [""] + column_headers,
                  "row_headers": ["Total Income", "Total Expenses"],
                  "summary": "Net Summary"
                  }
# Income Summary
income_summary = {"title": ["Income Summary", {"fore_color": white, "back_color": dark_green}],
                  "headers": [""] + column_headers,
                  "row_headers": ["Wages", "Tax Refund", "Rebates", "Gifts", "Deposits", "", "TOTAL Income"],
                  "summary": "Income Summary"
                  }
# Expense to Income tracker
expense_summary = {"title": ["Expense to Income", {"fore_color": black, "back_color": dark_orange}],
                   "headers": ["", "Budget", "As %", "Actual"],
                   "row_headers": ["Homes", "Necessity", "Personal", "Transportation", "Banking"],
                   "summary": "Total"
                }
# Home Expense, Necessity, Pet Necessity, Personal, Banking, Transport
home_expense = {"title": ["", {"fore_color": white, "back_color": dark_orange}],
                "headers": ["Home Expense"] + column_headers,
                "row_headers": ["Food", "Kitchen", "Pet Food", "Pet Litter", "Bed and Bath", "Health and Medical",  "Miscellaneous", ""],
                "summary": "Total Necessities"
                }
necessities =  {"title": ["", {"fore_color": white, "back_color": dark_orange}],
                "headers": ["Necessities"] + column_headers,
                "row_headers": ["Rent", "Hydro", "Internet", "Telephone", "Streaming", "Miscellaneous", ""],
                "summary": "Total Home Expenses"
                }
personal =  {"title": ["", {"fore_color": white, "back_color": dark_orange}],
            "headers": ["Personal"] + column_headers,
            "row_headers": ["Non-Alc Liquor", "Clothing", "Bed and Bath", "Medical", "Restaurants", "Miscellaneous", ""],
            "summary": "Total Personal"
            }
transport =  {"title": ["", {"fore_color": white, "back_color": dark_orange}],
            "headers": ["Transport"] + column_headers,
            "row_headers": ["Insurance", "Fuel", "Maintenance", "Automotive", "Fees/Fines", "Miscellaneous", ""],
            "summary": "Total Transport"
            }
banking =  {"title": ["", {"fore_color": white, "back_color": dark_orange}],
            "headers": ["Banking"] + column_headers,
            "row_headers": ["RRSP Contribution", "Fees", "Taxes", "Exchange", "Deposits", ""],
            "summary": "Total Banking"
            }
pet_expense =  {"title": ["", {"fore_color": white, "back_color": dark_orange}],
            "headers": ["Pet Expense"] + column_headers,
            "row_headers": ["Food", "Litter", "Medical", "Toys", "Miscellaneous", ""],
            "summary": "Total Pet Expense"
            }
