from datetime import datetime, timedelta
import pandas as pd

week = []

today = datetime.today()
start = today - timedelta(days=today.weekday())

for i in range(7):
    this = start + timedelta(days=i)
    week.append(this.strftime('%Y-%m-%d'))

print(week)

timesheet = pd.DataFrame(columns = week)

timesheet
