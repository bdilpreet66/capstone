
from validate_email import validate_email
from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from .models import Campaign, MessageInfo
from contacts.models import Contact
from user_information.models import Gmail, Outlook, Custom
from user_information import gmail_client, outlook_client, custom_client
from .common_functions import change_message, add_unsub_link
from googleapiclient.discovery import build

@shared_task(name="Send_Email")
def Send_Emails(campaign_id):
    obj = Campaign.objects.get(id=campaign_id)

    message = obj.message
    subject = obj.subject
    senderName = obj.display
    replyTo = obj.replyTo

    with open(obj.clist,'r') as f:
        data = f.read()
        data = data.split("|")
        contact_id = data.pop(0)
        data = "|".join(data)

    with open(obj.clist,'w') as f:
        f.write(data)

    obj.status = "started"
    obj.save()
    
    if obj.client == "Gmail":
        gmail_obj = Gmail.objects.get(user=obj.user)
        if gmail_obj.daily_limit_left != 0:
            if gmail_obj.active == True:
                gmail_obj.daily_limit_left -= 1
                gmail_obj.save()
                Send_Email_gmail.apply_async(
                    kwargs = {
                        'sender_email':gmail_obj.email,
                        'subject':subject,
                        'message':message,
                        'senderName':senderName,
                        'replyTo':replyTo,
                        'campaign_id':obj.id,
                        'client_id':gmail_obj.id,
                        'contact_id':contact_id
                    }
                )
    elif obj.client == "Outlook":
        outlook_obj = Outlook.objects.get(user=obj.user)
        if outlook_obj.daily_limit_left != 0:
            if outlook_obj.active == True:
                outlook_obj.daily_limit_left -= 1
                outlook_obj.save()
                Send_Email_outlook.apply_async(
                    kwargs = {
                        'sender_email':outlook_obj.email,
                        'subject':subject,
                        'message':message,
                        'senderName':senderName,
                        'replyTo':replyTo,
                        'campaign_id':obj.id,
                        'client_id':outlook_obj.id,
                        'contact_id':contact_id
                    }
                )
    elif obj.client == "Custom":
        custom_obj = Custom.objects.get(user=obj.user)
        if custom_obj.daily_limit_left != 0:
            if custom_obj.active == True:
                custom_obj.daily_limit_left -= 1
                custom_obj.save()
                Send_Email_custom.apply_async(
                    kwargs = {
                        'sender_email':custom_obj.smtpemail,
                        'subject':subject,
                        'message':message,
                        'senderName':senderName,
                        'replyTo':replyTo,
                        'campaign_id':obj.id,
                        'client_id':custom_obj.id,
                        'contact_id':contact_id
                    }
                )


################ GMAIL ##################

# Send email and schedule next
@shared_task(name="Send_Email_gmail",bind=True, max_retries=1, default_retry_delay=60*60*24)
def Send_Email_gmail(self,sender_email,subject,message,senderName,replyTo,campaign_id,client_id,contact_id):

    obj = Campaign.objects.get(id=campaign_id)
    cobj = Contact.objects.get(id=contact_id)
    gmail_obj = Gmail.objects.get(id=client_id)

    mobj = MessageInfo.objects.create(
        user = obj.user,
        campaign = obj,
        contact = cobj
    )

    with open(obj.clist,'r') as f:
        data = f.read()
        data = data.split("|")
        contact_id = data.pop(0)
        data = "|".join(data)

    if contact_id=="":
        obj.status = "finished"
        obj.save()
    else:
        with open(obj.clist,'w') as f:
            f.write(data)
    
        if gmail_obj.daily_limit_left != 0:
            gmail_obj.daily_limit_left -= 1
            if gmail_obj.active == True:
                gmail_obj.save()
                Send_Email_gmail.apply_async(
                    countdown = obj.time_delta,
                    kwargs = {
                        'sender_email':sender_email,
                        'subject':subject,
                        'message':message,
                        'senderName':senderName,
                        'replyTo':replyTo,
                        'campaign_id':campaign_id,
                        'client_id':gmail_obj.id,
                        'contact_id':contact_id
                    }
                )

    creds = gmail_client.get_saved_cred(client_id)

    with open(message,"r") as f:
        message = f.read()


    if validate_email(cobj.email):

        message = change_message(obj.id,mobj.id,message)

        if message.find("{ link }") != -1:
            message = add_unsub_link(obj.id,mobj.id,message)

        columns = ["first_name","last_name","address","email","bank","contact"]
        values = [cobj.first_name,cobj.last_name,cobj.address,cobj.email,cobj.bank,cobj.mobile]
        for i in range(len(columns)):
            name = "{ " + columns[i] + " }"
            if message.find(name):
                message = message.replace(name,values[i])
            if subject.find(name):
                subject = subject.replace(name,values[i])
            

        message = gmail_client.create_message(senderName,sender_email,cobj.email,subject,message,replyTo)

        service = build('gmail', 'v1', credentials=creds)

        message_sent = gmail_client.send_message(service,sender_email,message)

        if message_sent != False:
            if message_sent['labelIds'][0] == 'SENT':
                mobj.message_id = message_sent['id']
                mobj.email = cobj.email
                mobj.thread_id = message_sent['threadId']
                mobj.sent = True
                mobj.save()
                obj.sent_emails += 1
                obj.save()
    else:
        mobj.invalid = "yes"
        mobj.status = True
        mobj.save()
        obj.invalid += 1
        obj.save()

# reset daily email limit
@periodic_task(run_every=(crontab(hour=0,minute=0)), name="reset_gmail", ignore_result=True)
def reset_gmail():
    objs = Gmail.objects.filter(active=True)
    for obj in objs:
        obj.daily_limit_left = obj.emails_per_day
        obj.save()


################ Outlook ##################

# Send email and schedule next
@shared_task(name="Send_Email_outlook",bind=True, max_retries=1, default_retry_delay=60*60*24)
def Send_Email_outlook(self,sender_email,subject,message,senderName,replyTo,campaign_id,client_id,contact_id):

    obj = Campaign.objects.get(id=campaign_id)
    cobj = Contact.objects.get(id=contact_id)
    outlook_obj = Gmail.objects.get(id=client_id)

    mobj = MessageInfo.objects.create(
        user = obj.user,
        campaign = obj,
        contact = cobj
    )

    with open(obj.clist,'r') as f:
        data = f.read()
        data = data.split("|")
        contact_id = data.pop(0)
        data = "|".join(data)

    if contact_id=="":
        obj.status = "finished"
        obj.save()
    else:
        with open(obj.clist,'w') as f:
            f.write(data)
    
        if outlook_obj.daily_limit_left != 0:
            if outlook_obj.active == True:
                outlook_obj.daily_limit_left -= 1
                outlook_obj.save()
                Send_Email_outlook.apply_async(
                    countdown = obj.time_delta,
                    kwargs = {
                        'sender_email':sender_email,
                        'subject':subject,
                        'message':message,
                        'senderName':senderName,
                        'replyTo':replyTo,
                        'campaign_id':campaign_id,
                        'client_id':outlook_obj.id,
                        'contact_id':contact_id
                    }
                )

    with open(message,"r") as f:
        message = f.read()


    if validate_email(cobj.email):

        message = change_message(obj.id,mobj.id,message)

        if message.find("{ link }") != -1:
            message = add_unsub_link(obj.id,mobj.id,message)

        columns = ["first_name","last_name","address","email","bank","contact"]
        values = [cobj.first_name,cobj.last_name,cobj.address,cobj.email,cobj.bank,cobj.mobile]
        for i in range(len(columns)):
            name = "{ " + columns[i] + " }"
            if message.find(name):
                message = message.replace(name,values[i])
            if subject.find(name):
                subject = subject.replace(name,values[i])
            

        message = outlook_client.create_message(senderName,sender_email,cobj.email,subject,message,replyTo)

        outlook_client.send_message(message,outlook_obj.id)

        mobj.email = cobj.email
        mobj.sent = True
        mobj.save()
        
        obj.sent_emails += 1
        obj.save()
    else:
        mobj.invalid = "yes"
        mobj.status = True
        mobj.save()
        obj.invalid += 1
        obj.save()

# reset daily email limit
@periodic_task(run_every=(crontab(hour=0,minute=0)), name="reset_gmail", ignore_result=True)
def reset_outlook():
    objs = Outlook.objects.filter(active=True)
    for obj in objs:
        obj.daily_limit_left = obj.emails_per_day
        obj.save()


################ Custom ##################

# Send email and schedule next
@shared_task(name="Send_Email_custom",bind=True, max_retries=1, default_retry_delay=60*60*24)
def Send_Email_custom(self,sender_email,subject,message,senderName,replyTo,campaign_id,client_id,contact_id):

    obj = Campaign.objects.get(id=campaign_id)
    cobj = Contact.objects.get(id=contact_id)
    custom_obj = Custom.objects.get(id=client_id)

    mobj = MessageInfo.objects.create(
        user = obj.user,
        campaign = obj,
        contact = cobj
    )

    with open(obj.clist,'r') as f:
        data = f.read()
        data = data.split("|")
        contact_id = data.pop(0)
        data = "|".join(data)

    if contact_id=="":
        obj.status = "finished"
        obj.save()
    else:
        with open(obj.clist,'w') as f:
            f.write(data)
    
        if custom_obj.daily_limit_left != 0:
            if custom_obj.active == True:
                custom_obj.daily_limit_left -= 1
                custom_obj.save()
                Send_Email_custom.apply_async(
                    countdown = obj.time_delta,
                    kwargs = {
                        'sender_email':sender_email,
                        'subject':subject,
                        'message':message,
                        'senderName':senderName,
                        'replyTo':replyTo,
                        'campaign_id':campaign_id,
                        'client_id':custom_obj.id,
                        'contact_id':contact_id
                    }
                )

    with open(message,"r") as f:
        message = f.read()


    if validate_email(cobj.email):

        message = change_message(obj.id,mobj.id,message)

        if message.find("{ link }") != -1:
            message = add_unsub_link(obj.id,mobj.id,message)

        columns = ["first_name","last_name","address","email","bank","contact"]
        values = [cobj.first_name,cobj.last_name,cobj.address,cobj.email,cobj.bank,cobj.mobile]
        for i in range(len(columns)):
            name = "{ " + columns[i] + " }"
            if message.find(name):
                message = message.replace(name,values[i])
            if subject.find(name):
                subject = subject.replace(name,values[i])
            

        message = custom_client.create_message(senderName,sender_email,cobj.email,subject,message,replyTo,custom_obj.imapemail)

        custom_client.send_message(message,custom_obj.id)

        mobj.email = cobj.email
        mobj.sent = True
        mobj.save()
        
        obj.sent_emails += 1
        obj.save()
    else:
        mobj.invalid = "yes"
        mobj.status = True
        mobj.save()
        obj.invalid += 1
        obj.save()

# reset daily email limit
@periodic_task(run_every=(crontab(hour=0,minute=0)), name="reset_gmail", ignore_result=True)
def reset_custom():
    objs = Custom.objects.filter(active=True)
    for obj in objs:
        obj.daily_limit_left = obj.emails_per_day
        obj.save()
