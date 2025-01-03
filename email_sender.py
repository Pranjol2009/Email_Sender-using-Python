import smtplib



sender_email=input("Enter sender email: ")

receiver_email=input("Enter receiver email: ")

subject=input("Enter subject: ")

message=input("Enter message: ")

body=f"Subject:{subject}\n\n{message}"










email_server=smtplib.SMTP("smtp.gmail.com",587)



email_server.starttls()

email_server.login(sender_email,"xcvw hfcs dlfk kqje")


email_server.sendmail(sender_email,receiver_email,body)


print("Email sent successfully")