import smtplib,ssl



def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "shashwatsandilya514@gmail.com"
    password = "lpfkgredjbowjmhk"



    receiver = "shashwatsandilya514@gmail.com"

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=my_context) as server:
        server.login(user_name,password)
        server.sendmail(user_name,receiver,message)