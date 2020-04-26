import os # to use my env vars
import smtplib # to send emails

# getting my gmail credentials 
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() # identification
    smtp.starttls() # encrypting the traffic
    smtp.ehlo() # encrypted identification

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # login to my gmail account

    subject = 'Hi BUBU'
    body = 'MA KORE?'

    msg = f'Subject: {subject}\n\n{body}' # building the message

    smtp.sendmail(EMAIL_ADDRESS, 'noamir2512@gmail.com', msg)

