# Helpers for the users app
import smtplib
# import getpass

def sendMail(to,subject,message,pwd):

    
    smtp_obj = smtplib.SMTP("smtp.gmail.com",587)
    print(smtp_obj.starttls())

    # email = getpass.getpass("Email:")
    # pwd = getpass.getpass("Password:")
    print(smtp_obj.login(from_email,pwd))
    # awpk yyif fswh jcce

    
    msg = "Subject:"+subject+"\n"+message

    smtp_obj.sendmail(from_email,to,msg)