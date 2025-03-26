import smtplib

# Your email credentials
SENDER_EMAIL = "takurganig@gmail.com"
RECEIVER_EMAIL = "cherugad5@gmail.com"
APP_PASSWORD = "takurganig@1234"  # Use an app password, not your actual Gmail password

# Create SMTP session
smtObj = smtplib.SMTP("smtp.gmail.com", 587)
smtObj.ehlo()  # Identify to the mail server
smtObj.starttls()  # Secure the connection

# Login with App Password
smtObj.login(SENDER_EMAIL, APP_PASSWORD)

# Prepare the email message properly
subject = "SMTP Check"
body = "This is a test email using Python."
message = f"Subject: {subject}\n\n{body}"

# Send the email
smtObj.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)

# Close the connection
smtObj.quit()

print("✅ Email sent successfully!")
