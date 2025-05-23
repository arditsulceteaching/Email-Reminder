import csv
import smtplib
from email.message import EmailMessage

with open("reminders.csv") as file:
    reader = csv.DictReader(file)
    reminders = list(reader)

print(reminders)

for r in reminders:
    msg = EmailMessage()
    msg['Subject'] = "⏰ Your Reminder for Today"
    msg['From'] = "app10flask@gmail.com"
    msg['To'] = r['email']
    msg.set_content(f"Message: {r['message']}\n"
                    f"Date: {r['date']}\n"
                    f"Time: {r['time']}")
    print(msg)