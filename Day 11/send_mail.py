import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

# environment variables
username = ''
password = ''

class Emailer():
    subject = ""
    to_emails = []
    from_email='Hungry Py <muhammaduktamoof@gmail.com>'
    def __init__(self, text, subject="", template_name=None, context={}, template_html=None, to_emails=None):
        if template_name == None and template_html == None:
            raise Exception ("You must set a template")
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.subject = subject

    def send_mail(text='Email Body', subject='Hello World', to_emails=None, html=None):
        
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject

        txt_part = MIMEText(text, 'plain')
        msg.attach(txt_part)
        if html != None:
            html_part = MIMEText(html, 'html')
            msg.attach(html_part)
        msg_str = msg.as_string()

        # login to my smtpserver
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg_str)
        server.quit()    