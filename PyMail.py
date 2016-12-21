# Email Message Sending from Pytho

import smtplib

# Email Credentials
toAddr = raw_input("Recipient's Email Address: ")
fromAddrUser = raw_input("Sender's Email Address: ")
fromAddrPassword = raw_input("Password: ")

# Email Content
emailSubject = raw_input("Subject: ")
emailMessage = raw_input("Message: ")

# Email Server
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(fromAddrUser, fromAddrPassword)

# Email Header
emailHeader = 'To:' + toAddr + '\n' + 'From: ' + fromAddrUser + '\n' + 'Subject: ' + emailSubject + '\n'
print '\n' + emailHeader

# Email Message
fullMessage = emailHeader + '\n' + emailMessage + '\n\n'
smtpserver.sendmail(fromAddrUser, toAddr, fullMessage)

print 'Email sent'

smtpserver.close()
