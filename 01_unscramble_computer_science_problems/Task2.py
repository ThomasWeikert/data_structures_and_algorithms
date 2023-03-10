"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from itertools import groupby
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_durations = defaultdict(int)
for call in calls:
    call_durations[call[0]] += int(call[3])
    call_durations[call[1]] += int(call[3])

max_call_nb = max(call_durations, key=call_durations.get)
max_call_duration = call_durations[max_call_nb]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_call_nb, max_call_duration))