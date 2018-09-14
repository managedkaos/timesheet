from datetime import datetime, time, timedelta
from hashlib import sha1
import json
import random
import string

PROJECTS = ['A', 'B', 'C', 'X']

frames = []

today = datetime.today()
monday = today - timedelta(days=today.weekday())

for i in range(5):
    frame_id = sha1()
    date = monday + timedelta(days=i)
    hour = 8

    for project in PROJECTS:
        start = datetime(date.year, date.month, date.day, hour, 0)
        hour = hour + 2
        stop = datetime(date.year, date.month, date.day, hour, 0)

        # skip an hour for lunch
        hour = 13 if hour == 12 else hour

        # update the frame_id
        seed = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
        frame_id.update(seed.encode())

        frames.append([int(start.timestamp()),
                       int(stop.timestamp()),
                       "Project_{}".format(project),
                       str(frame_id.hexdigest()),
                       [],
                       int(stop.timestamp())])

print(json.dumps(frames, indent=1))
