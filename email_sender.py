import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails(user_email_addr, user_password_val, receiver_email_addrs, email_subject, email_message, is_html_format, names):
    try:
        # Set up the SMTP server and login
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(user_email_addr, user_password_val)
        
        successful_emails = []
        unsuccessful_emails = []

        for receiver_email_addr, name in zip(receiver_email_addrs, names):
            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = user_email_addr
            msg["To"] = receiver_email_addr
            msg["Subject"] = email_subject.replace("[Name]", name)

            # Set the message body based on the chosen format (plain text or HTML)
            if is_html_format:
                message_body = email_message.replace("[Name]", name)
                msg.attach(MIMEText(message_body, "html"))
            else:
                message_body = email_message.replace("[Name]", name)
                msg.attach(MIMEText(message_body, "plain"))

            # Send the email
            smtp_server.sendmail(user_email_addr, receiver_email_addr, msg.as_string())

        # Quit the SMTP server
        smtp_server.quit()

        return True, "Emails sent successfully!"
    except Exception as e:
        return False, f"Error sending emails: {e}"
