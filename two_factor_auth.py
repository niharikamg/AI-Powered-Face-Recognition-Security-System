import pyotp
import smtplib

def send_otp(email):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=30)
    otp = totp.now()

    sender_email = "your_email@gmail.com"
    receiver_email = email
    password = "your_email_password"

    subject = "Your Security OTP"
    body = f"Your OTP is {otp}. It expires in 30 seconds."

    message = f"Subject: {subject}\n\n{body}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

    return otp, totp
