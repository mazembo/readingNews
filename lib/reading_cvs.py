import csv

f = open('attendees1.csv')
csv_f = csv.reader(f)
attendees1 = []
for row in csv_f:
    attendees1.append(row[2])
f.close()

f = open('attendees2.csv')
csv_f = csv.reader(f)
attendees2 = []
for row in csv_f:
    attendees2.append(row[2])
f.close

attendees1 = set(attendees1)
attendees2 = set(attendees2)

print attendees2.difference(attendees1)
