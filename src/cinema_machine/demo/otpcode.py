from flask import Flask, request, jsonify
import smtplib
import random
import time
from email.mime.text import MIMEText

app = Flask(__name__)

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

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    otp = generate_otp()

    otp_storage[email] = {
        "otp": otp,
        "time": time.time()
    }

    try:
        send_email(email, otp)
        return jsonify({"message": "OTP sent"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.json
    email = data.get("email")
    user_otp = data.get("otp")

    if email not in otp_storage:
        return jsonify({"error": "No OTP found"}), 400

    saved = otp_storage[email]

    if time.time() - saved["time"] > 300:
        del otp_storage[email]
        return jsonify({"error": "OTP expired"}), 400

    if user_otp == saved["otp"]:
        del otp_storage[email]
        return jsonify({"message": "Verified"})
    else:
        return jsonify({"error": "Invalid OTP"}), 400

if __name__ == "__main__":
    app.run(debug=True)