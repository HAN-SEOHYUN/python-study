import smtplib
from email.mime.text import MIMEText
import dotenv
import os
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

send_email = "h0031271@gmail.com"
send_pwd = os.environ['GOOGLE_PASSWORD']

recv_email = "h0031271@naver.com"

smtp_name="smtp.gmail.com"
smtp_port=587

text="""
메일 내용
"""
msg = MIMEText(text)

msg['Subject'] = "메일제목"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name, smtp_port )
s.starttls()
s.login( send_email, send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()