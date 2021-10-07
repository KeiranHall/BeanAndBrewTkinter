import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(email, details):
    sender_email = "beanandbrewmail@gmail.com"
    receiver_email = email
    password = "zzxjoufnojsxziae"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Bean and Brew Booking confirmation"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = """\
    <!DOCTYPE html>
    <html>

    <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    </head>

    <body>
        <div style="font-family: 'Montserrat', sans-serif;text-align: center;margin-left: 20%;margin-right: 20%;">
            <div class="wrapper" style="border: 2px solid black;background: rgb(228, 227, 227);">
                    <h1>Bean and Brew</h1>
                    <p>Thanks for booking a table with us and we can't wait to welcome you to our amazing resturants. Here are you booking
                            details</p>
                    <div class="details" style="margin-left: 20%;margin-right: 20%;padding: 5px;background: white;">
                        <h3>{branch}, {table}</h3>
                    </div>
                    <p>If you have an concerns or questions please fell free to reply to this email</p>
            </div>
    </body>

    </html>""".format(branch=details["branch"], table=details["tableNum"], subtype='html')

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
