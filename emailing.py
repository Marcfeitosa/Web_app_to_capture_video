import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "your password here"
SENDER = "Your e-mail here"
RECEIVER = "The e-mail you want to receive the message"

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imgdhr.what(None, content))

    # This is the process for gmail it is going to be different for each provider. You can find it on the web how it is done
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")

if __name__ == "__main__":
    send_email(image_path="images/19.png")