import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email credentials
your_email = 'you@example.com'
your_password = 'your_password'

# Recipient's email address
recipient_email = 'recipient@example.com'

# Email subject
subject = 'Email with HTML Table'

# Data for the table
data = [
    {
        'Product': 'Product 1',
        'Price': 120.50,
        'Quantity': 15,
        'In Stock': True
    },
    {
        'Product': 'Product 2',
        'Price': 199.99,
        'Quantity': 8,
        'In Stock': False
    }
]

# Generate the HTML table
html_message = '<html><body><table border="1" cellspacing="0" cellpadding="5">'

# Add table headers
html_message += '<tr>'
for header in data[0].keys():
    html_message += f'<th>{header}</th>'
html_message += '</tr>'

# Add table rows
for row in data:
    html_message += '<tr>'
    for cell in row.values():
        html_message += f'<td>{cell}</td>'
    html_message += '</tr>'

html_message += '</table></body></html>'

# Create a MIMEText object for the message
msg = MIMEMultipart()
msg.attach(MIMEText(html_message, 'html'))

# Set email headers
msg['From'] = your_email
msg['To'] = recipient_email
msg['Subject'] = subject

# Connect to the email server and send the email
try:
    # Create an SMTP session and start TLS encryption
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()

    # Log in to the email server
    server.login(your_email, your_password)

    # Send the email
    server.sendmail(your_email, recipient_email, msg.as_string())

    # Close the connection to the email server
    server.quit()

    print('Email sent successfully!')
except Exception as e:
    print(f'Error sending email: {e}')
