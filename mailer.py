import smtplib
from email.mime.text import MIMEText
from log_config import setup_logger


logger = setup_logger('system_log', 'systemlog.log')


def send_email(subject, message, recipients):
    sender = "your_email@example.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    try:
        with smtplib.SMTP('smtp.example.com', 25) as server:
            server.set_debuglevel(1)
            server.sendmail(sender, recipients, msg.as_string())
            logger.info("Email sent to %s", ", ".join(recipients))
    except Exception as e:
        logger.error("Failed to send email: %s", str(e))
