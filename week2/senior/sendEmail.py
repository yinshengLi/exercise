#__author:iruyi
#date:2018/9/21
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'iruyingsuixing@163.com'
receivers = ['2772315248@qq.com']
host = 'smtp.163.com'
port = '465'#或994
password = 'ilovedj1314'



message = MIMEText('Python test', 'plain', 'utf-8')
message['From'] = Header('菜鸟', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = 'Python 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host, port)
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('send success')
except smtplib.SMTPException:
    print('Error: 无法发送')