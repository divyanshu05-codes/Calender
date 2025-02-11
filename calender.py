import calendar

def create_calendar(year, month):
    cal = calendar.TextCalendar()
    calendar_text = cal.formatmonth(year, month)
    print(calendar_text)
year =int(input("Enter the Year:"))
month =int(input("Enter the  Month:"))
create_calendar(year, month)
