import smtplib
from email.mime.text import MIMEText
import yaml
import logging

def send_email(subject, body, to_addrs):
    with open('config/settings.yml', 'r') as file:
        config = yaml.safe_load(file)

    email_settings = config['email_settings']
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_settings['username']
    msg['To'] = to_addrs

    try:
        with smtplib.SMTP(email_settings['smtp_server'], email_settings['smtp_port']) as server:
            server.starttls()
            server.login(email_settings['username'], email_settings['password'])
            server.sendmail(email_settings['username'], [to_addrs], msg.as_string())
        logging.info(f"Email sent to {to_addrs}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_addrs}: {e}")

if __name__ == "__main__":
    import sys
    subject = sys.argv[1]
    body = sys.argv[2]
    to_addrs = sys.argv[3]
    send_email(subject, body, to_addrs)
