import smtplib
#help(smtplib)
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('justkiddingboat@gmail.com','just123kidding')
