import random
import smtplib
import datetime


MY_EMAIL = "orkazazgithub@gmail.com"
MY_PASS = "Notarealpassatall"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_files:
        all_quotes = quote_files.readline()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")
