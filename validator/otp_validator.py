import random
import smtplib
import time
from email.message import EmailMessage

# Server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

from_mail = "qldbvillatura@tip.edu.ph"
app_password = "ksoa zqlm aiul wrjk"
server.login(from_mail, app_password)


# Generate OTP
def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))

    return otp


def send_otp(to_mail):
    otp = generate_otp()
    print(otp)
    otp_time = time.time()
    msg = EmailMessage()
    msg['Subject'] = 'MOON HEY HOTPOT OTP VERIFICATION CODE'
    msg['From'] = from_mail
    msg['To'] = to_mail

    message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .otp-box {{
                border: 2px solid #036666;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }}
            .otp-code {{
                font-size: 24px;
                color: #036666;
            }}
            p {{
                color: black;
            }}
        </style>
    </head>
    <body>
        <p>Your One-Time Password (OTP) is:</p>

        <div class="otp-box">
            <p class="otp-code">{otp}</p>
        </div>

        <p>This code is valid for the next 5 minutes. Please do not share this code with anyone. If you did not request this OTP, please contact your manager immediately.</p>
    </body>
    </html>
    """

    msg.add_alternative(message, subtype='html')

    server.send_message(msg)
    print('Email Sent')

    return otp, otp_time
