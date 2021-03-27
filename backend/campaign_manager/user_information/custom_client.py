import smtplib
import imaplib
from email import message_from_string
from email.message import EmailMessage
from .models import Custom
from datetime import datetime



def create_message(sender_name,sender,reciever,subject,message,reply_to,bounce_address):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = f"{sender_name}<{sender}>"
    msg['To'] = reciever
    msg['Reply-To'] = reply_to
    msg['Return-Path'] = bounce_address
    msg['Mail-From'] = bounce_address
    
    msg.add_alternative(message,subtype="html")
    
    return msg


def send_message(message,client_id):
    obj = Custom.objects.get(id=client_id)

    USERNAME = obj.smtpusername
    PASSWORD = obj.smtp_password
    smtp_host = obj.smtp_host
    smtp_port = obj.smtp_port

    if obj.smtp_type == "STARTTLS":
        with smtplib.SMTP(smtp_host,smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(USERNAME,PASSWORD)

            smtp.send_message(message)

    elif obj.smtp_type == "Enable SSL":
        with smtplib.SMTP_SSL(smtp_host,smtp_port) as smtp:
            smtp.login(USERNAME,PASSWORD)

            smtp.send_message(message)


def get_bounced_emails(client_id,email_list):
    obj = Custom.objects.get(id=client_id)

    USERNAME = obj.imapusername
    PASSWORD = obj.IMAP_password
    imap_host = obj.IMAP_host
    imap_port = obj.IMAP_port

    emails = []

    if obj.IMAP_type == "Enable SSL": 
        with imaplib.IMAP4_SSL(imap_host,imap_port) as conn:

            try:
                result = conn.login(USERNAME,PASSWORD)
            except:
                return emails

            if result[0] == "OK":
                result = conn.select("INBOX")
                if result[0] == "OK":
                    result,data = conn.search(None, '(UNSEEN)')
                    if result == "OK":
                        if data[0] != b'':
                            for email_id in data[0].split():
                                result, email = conn.fetch(email_id,'(RFC822)')
                                if result == "OK":
                                    email = email[0][1].decode("utf-8")
                                    myemail = message_from_string(email)
                                date = myemail['Date']
                                for i in get_three_days():
                                    if f' {i} ' in date:
                                        myemail = myemail.get_payload(1)
                                        try:
                                            myemail = myemail.get_payload(1)
                                            if myemail['Action'] == "failed":
                                                if str(myemail['X-Display-Name']) in email_list:
                                                    emails.append(myemail['X-Display-Name'])
                                                    conn.store(email_id, '+FLAGS', '\\Deleted')
                                                    conn.expunge()
                                                else:
                                                    conn.store(email_id, '+FLAGS', '\\UNSEEN')
                                                    conn.expunge()
                                        except:
                                            pass
                        else:
                            pass

    elif obj.IMAP_type == "STARTTLS":
        with imaplib.IMAP4(imap_host,imap_port) as conn:
            conn.starttls()
            
            try:
                result = conn.login(USERNAME,PASSWORD)
            except:
                return emails
            
            if result[0] == "OK":
                result = conn.select("INBOX")
                if result[0] == "OK":
                    result,data = conn.search(None, f'(UNSEEN)')
                    if result == "OK":
                        if data[0] != b'':
                            for email_id in data[0].split():
                                result, email = conn.fetch(email_id,'(RFC822)')
                                if result == "OK":
                                    email = email[0][1].decode("utf-8")
                                    myemail = message_from_string(email)
                                date = myemail['Date']
                                for i in get_three_days():
                                    if f' {i} ' in date:
                                        myemail = myemail.get_payload(1)
                                        try:
                                            myemail = myemail.get_payload(1)
                                            if myemail['Action'] == "failed":
                                                if str(myemail['X-Display-Name']) in email_list:
                                                    emails.append(myemail['X-Display-Name'])
                                                    conn.store(email_id, '+FLAGS', '\\Deleted')
                                                    conn.expunge()
                                                else:
                                                    conn.store(email_id, '+FLAGS', '\\UNSEEN')
                                                    conn.expunge()
                                        except:
                                            pass
                        else:
                            pass

    return emails



def get_three_days():
    now = datetime.now().day
    if now == 1:
        prev = 31
        prev_2 = 30
    elif now == 2:
        prev = 1
        prev_2 = 31
    else:
        prev = now-1
        prev_2 = prev-1
        
    return now,prev,prev_2