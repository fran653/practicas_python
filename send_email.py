from email.message import EmailMessage
import smtplib
import getpass

# Get password securely
mail_pass = getpass.getpass('Password? ')

# Initialize SMTP server
mail_server = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
mail_server.set_debuglevel(1)


# Login to the mail server
sender = "x@hotmail.com"
recipient = "y@hotmail.com"

# Create email message
message = EmailMessage()
message['From'] = sender
message['To'] = recipient
print(message)
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content("This is a test email sent from Python!")

# Print message for debugging
print(message)

# Close the connection
mail_server.quit()

