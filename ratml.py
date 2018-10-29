# prog for sending n receiving a mail
import smtplib
import getpass
print("enter your email id.")
email=input()
print("enter your password.")
pwd=getpass.getpass()
print("enter the receiver's email id.")
rmail=input()
#create smtp session
s=smtplib.SMTP('smtp.gmail.com',587)
#start TLS for security
s.starttls()
# authentication
s.login(email,pwd)
# msg to be sent
print(" enter the message.")
msg=input()
# sending the mail
s.sendmail(email,rmail,msg)
# terminating
s.quit()