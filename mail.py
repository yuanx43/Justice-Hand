#!/usr/bin/python
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Which email address want to send
# 明文的帳密
to = ''

# Using specific gmail account
gmail_user = ''
gmail_password = ''

# SMTP command
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

# Linux Specific shell command
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].decode().split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'Your ip is %s' %  ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
