#! /usr/bin/env python3
 # smtp_email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials and server configuration
SMTP_SERVER = 'mail.pythonhat.com'
SMTP_PORT = 465
EMAIL = 'smtp_admin@pythonhat.com'  # Replace with your email
PASSWORD = 'h3'        # Replace with your password

# Email content
recipient = 'ezalahmad@gmail.com'  # Replace with recipient's email
subject = 'Test Email for FastAPI app'
body = 'This is a test email sent with SSL/TLS.'

# Create the email
message = MIMEMultipart()
message['From'] = EMAIL
message['To'] = recipient
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server using SSL
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, PASSWORD)  # Log in to the server
        server.sendmail(EMAIL, recipient, message.as_string())  # Send email
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

