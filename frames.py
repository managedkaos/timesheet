''' Module: frames.py - A Watson frames generator'''
from datetime import datetime, timedelta
from hashlib import sha1
import json
import random
import string

PROJECTS = ['A', 'B', 'C', 'X']

FRAMES = []

TODAY = datetime.today()
MONDAY = TODAY - timedelta(days=TODAY.weekday())

for i in range(5):
    frame_id = sha1()
    date = MONDAY + timedelta(days=i)
    hour = 8

    for project in PROJECTS:
        start = datetime(date.year, date.month, date.day, hour, 0)
        hour = hour + 2
        stop = datetime(date.year, date.month, date.day, hour, 0)

        # skip an hour for lunch
        hour = 13 if hour == 12 else hour

        # update the frame_id
        seed = ''.join(random.choice(string.ascii_uppercase + string.digits)
                       for _ in range(32))
        frame_id.update(seed.encode())

        FRAMES.append([int(start.timestamp()),
                       int(stop.timestamp()),
                       "Project_{}".format(project),
                       str(frame_id.hexdigest()),
                       [],
                       int(stop.timestamp())])

print(json.dumps(FRAMES, indent=1))
