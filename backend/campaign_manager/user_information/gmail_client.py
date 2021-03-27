from __future__ import print_function

import argparse
import base64
import os.path
import pickle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
# from .models import profile
# from schedules.models import campaign, email_list

# from .common_functions import add_unsub_link, change_message
from .models import Gmail

SCOPES = ['https://mail.google.com/']

def get_auth_url():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # If there are no (valid) credentials available, let the user log in.
    flow = Flow.from_client_secrets_file(
        'user_information/credentials_gmail.json', SCOPES, redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    return flow.authorization_url(prompt='consent')

def get_cred_from_token(code):
    flow = Flow.from_client_secrets_file(
        'user_information/credentials_gmail.json', SCOPES, redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    flow.fetch_token(code=code)
    creds = flow.credentials
    service = build('gmail', 'v1', credentials=creds)
    email = service.users().getProfile(userId="me").execute()["emailAddress"]
    return creds,email

def get_saved_cred(id):
    obj = Gmail.objects.get(id=id)
    file_name = obj.key
    creds = None
    if os.path.exists(file_name):
        with open(file_name, 'rb') as token:
            creds = pickle.load(token)
            
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                return creds
            else:
                obj.active = False
                obj.save()
        else:
            return creds
    else:
        obj.active = False
        obj.save()



def create_message(senderName,sender, to, subject, message_text,reply_to):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text,'html')
    message['to'] = to
    message['from'] = f"{senderName}<{sender}>"
    message['subject'] = subject
    
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, user_id, message):
    """Send an email message.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

    Returns:
        Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                .execute())
        return message
    except:
        return False
        

def get_bounced_emails(service,thread_id):
    tdata = service.users().threads().get(userId='me', id=thread_id).execute()
    
    try:
        info = tdata['messages'][1]["payload"]["headers"]
        for data in info:
            if data["name"] == "From" and ("mailer-daemon@googlemail.com" in data["value"] or "mailer-daemon@google.com" in data["value"]):
                email_list_obj = email_list.objects.get(thread_id = thread_id)
                campaign_obj = campaign.objects.get(id = email_list_obj.campaign.id)
                email_list_obj.bounced = True
                email_list_obj.status = True
                campaign_obj.bounced += 1
                campaign_obj.save()
                email_list_obj.save()
                service.users().threads().delete(userId='me', id=thread_id).execute()
    except:
        email_list_obj = email_list.objects.get(thread_id = thread_id)
        campaign_obj = campaign.objects.get(id = email_list_obj.campaign.id)
        campaign_obj.delivered += 1
        campaign_obj.save()
        email_list_obj.status = True
        email_list_obj.save()
        service.users().threads().delete(userId='me', id=thread_id).execute()


