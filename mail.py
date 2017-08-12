import smtplib

server = 'smtp.gmail.com'
user = '<username>@gmail.com'
password = 'password123123'

recipients = ['<recipients comma separated email ids']
sender = '<sender>@gmail.com'
message = 'Hello World'

session = smtplib.SMTP(server)
session.ehlo()
session.starttls()
session.login(user, password)
session.sendmail(sender, recipients, message)