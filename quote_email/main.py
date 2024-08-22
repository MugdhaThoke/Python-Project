import random
import smtplib
#
# my_email = "mugdhathoke0909@gmail.com"
# password = "ypbavagyghqdukqx"
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="mugdha0909@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my mail")


import datetime as dt

# now =dt.datetime.now()
# print(type(now.year))
# print(now.day)
# print(now.month)
# print(now.hour)
# print(now.minute)
# print(now.weekday())
# year = now.year
# if year == 2024:
#     print("Wear a mask")
#
# date_of_birth = dt.datetime(year=2003, month=9, day=9,hour=9)
# print(date_of_birth)

my_email = "mugdhathoke0909@gmail.com"
password = "ypbavagyghqdukqx"

now =dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # print(quote)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mugdha0909@yahoo.com",
                            msg=f"Subject:Thursday Motivation \n\n{quote}")