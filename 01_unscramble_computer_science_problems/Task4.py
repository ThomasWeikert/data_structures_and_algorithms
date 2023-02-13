"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = [item[0] for item in calls]
incoming_calls = [item[1] for item in calls]

outgoing_texts = [item[0] for item in texts]
incoming_texts = [item[1] for item in texts]


def is_fraudulent(number: str):
    if number in (incoming_calls + outgoing_texts + incoming_texts):
        return False
    else: 
        return True 

pot_tele_marketing_nb = set()
for record in outgoing_calls:
    if is_fraudulent(record):
        pot_tele_marketing_nb.add(record)

print("These numbers could be telemarketers: ")
print(*sorted(pot_tele_marketing_nb), sep='\n')




