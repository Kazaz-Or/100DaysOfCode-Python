import datetime
import smtplib
import pandas
import random

MY_MAIL = "orkazazgithub@gmail.com"
PASS = "notarealpass"

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL, PASS)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
