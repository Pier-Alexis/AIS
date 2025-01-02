import smtplib
from email.message import EmailMessage

def send_alert(subject, body):
    sender_email = "your_email@gmail.com"
    receiver_email = "destinator@gmail.com"
    password = "your_passwd"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Alert sended with sucess.")
    except Exception as e:
        print(f"Error while sending the alert : {e}")
