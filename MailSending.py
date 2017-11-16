import smtplib
import socks

#socks.setdefaultproxy(TYPE, ADDR, PORT)
socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, 'proxy.proxy.com')
socks.wrapmodule(smtplib)

smtpserver = 'smtp.gmail.com'
AUTHREQUIRED = 1
smtpuser = 'sukumarsuku222@gmail.com'
smtppass = 'mypassword'

RECIPIENTS = 'sukumarsuku222@gmail.com'
SENDER = 'sukumarsuku222@gmail.com'
mssg = "test message"
s = mssg

server = smtplib.SMTP(smtpserver,587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(smtpuser,smtppass)
server.set_debuglevel(1)
server.sendmail(SENDER, [RECIPIENTS], s)
server.quit()
