import smtplib

conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('quench2k20.bbs@gmail.com', '7749265@Pn')
message = input("Enter Your message")

conn.sendmail('quench2k20.bbs@gmail.com','priyank.ninama@gmail.com', message)
conn.quit()