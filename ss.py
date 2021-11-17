import random
import smtplib

gmail_user = 'YOUR EMAIL'
gmail_password = 'YOUR EMAIL PASSWORD'

participantes = {'PERSON 01': 'THEIR EMAIL',
                 'PERSON 02': 'THEIR EMAIL',
                 'PERSON 03': 'THEIR EMAIL',
                 'PERSON 04': 'THEIR EMAIL',
                 'PERSON 05': 'THEIR EMAIL',
                 'PERSON 06': 'THEIR EMAIL'
                 }

buyers = [*participantes]
recievers = [*participantes]

random.shuffle(buyers)
random.shuffle(recievers)


flag = True
counter = 0

while flag or counter > 6:
    for i in range(0, len(buyers)):
        if buyers[i] == recievers[i]:
            random.shuffle(recievers)
            counter += 1
            if buyers[i] == recievers[i]:
                random.shuffle(buyers)
        else:
            flag = False
for i in range(len(buyers)):

    to = [participantes[buyers[i]]]
    sent_from = gmail_user
    subject = 'secret santa draw'
    body = "Hey, what's up? Hope you're liking your holidays, this year you'll be buying a gift for " + recievers[i] + \
           "\n\n-Python program"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

if __name__ == '__main__':
    pass
