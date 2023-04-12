import datetime

today = datetime.date.today()
month = today.month
year = today.year

dates = []

while len(dates) < 18:
    d = datetime.date(year, month, 1)
    while d.weekday() != 4:
        d += datetime.timedelta(days=1)
    d += datetime.timedelta(days=7)
    dates.append("Friday, " + d.strftime("%B %d, %Y"))
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

output = "\n".join(dates)
print(output)
