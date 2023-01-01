import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import os

GM_KEY = os.getenv("GM_KEY")
EMAIL_KEY = os.getenv("EMAIL_KEY")

def tt_email(name):

  html = Template(Path('./templates/message.html').read_text())
  email = EmailMessage()
  email['from'] = 'Tony Thomas'
  email['to'] = 'tonythomas001@hotmail.co.uk'
  email['subject'] = 'Somebody called by your website today'

  email.set_content(html.substitute({'name': name},), 'html')

  with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login({EMAIL_KEY}, {GM_KEY})
    smtp.send_message(email)
    # print('all good boss!')

# (tt_email('tony thomas called to say hello'))