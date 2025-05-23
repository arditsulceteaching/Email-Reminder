import csv

with open("reminders.csv") as file:
    reader = csv. DictReader(file)
    reminders = list(reader)

print(reminders)

