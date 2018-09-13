from datetime import datetime, timedelta
from tabulate import tabulate
import json
import pandas as pd
import subprocess

timesheet = pd.DataFrame()

today = datetime.today()
start = today - timedelta(days=today.weekday())

for i in range(7):
    date = (start + timedelta(days=i)).strftime('%Y-%m-%d')
    report = subprocess.Popen(['watson', 'report', '--json',
          '--from', date,
          '--to', date],
          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = report.communicate()
    data = json.loads(stdout.decode('utf8'))

    timesheet.at['Total', date] = str(timedelta(seconds=data['time']))

    for project in data['projects']:
        timesheet.at[project['name'], date] = str(timedelta(seconds=project['time']))

timesheet.fillna('', inplace=True)
print(tabulate(timesheet, headers='keys', tablefmt='psql'))

