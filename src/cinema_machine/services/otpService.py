import smtplib
import random
import time
from email.mime.text import MIMEText

otp_storage = {}

def generate_otp():
    return str(random.randint(100000, 999999))


def send_email(receiver_email, otp):
    sender_email = "ticketscinemasupport@gmail.com"
    app_password = "asyv pgbx jkuj dzzv"

    msg = MIMEText(f"Your OTP is {otp}. It expires in 5 minutes.")
    msg["Subject"] = "Your OTP Code"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()


def create_and_send_otp(email: str):
    otp = generate_otp()

    otp_storage[email] = {
        "otp": otp,
        "time": time.time()
    }

    send_email(email, otp)


def verify_otp(email: str, user_otp: str):
    if email not in otp_storage:
        return False, "No OTP found"

    saved = otp_storage[email]

    if time.time() - saved["time"] > 300:
        del otp_storage[email]
        return False, "OTP expired"

    if user_otp == saved["otp"]:
        del otp_storage[email]
        return True, "OTP verified"

    return False, "Invalid OTP"