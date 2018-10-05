''' Module: timesheet.py - A timesheet generator'''
import json
import subprocess
from datetime import datetime, timedelta
import pandas as pd
from tabulate import tabulate

TIMESHEET = pd.DataFrame()

TODAY = datetime.today()
START = TODAY - timedelta(days=TODAY.weekday())

for i in range(7):
    date = (START + timedelta(days=i)).strftime('%Y-%m-%d')
    report = subprocess.Popen(['watson', 'report', '--json',
                               '--from', date,
                               '--to', date],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    stdout, stderr = report.communicate()
    data = json.loads(stdout.decode('utf8'))

    TIMESHEET.at['Total', date] = str(timedelta(seconds=data['time']))

    for project in data['projects']:
        TIMESHEET.at[project['name'],
                     date] = str(timedelta(seconds=project['time']))

TIMESHEET.fillna('', inplace=True)
print(tabulate(TIMESHEET, headers='keys', tablefmt='psql'))
