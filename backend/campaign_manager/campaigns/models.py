from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact


class Template(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255,default="")
    subject = models.CharField(max_length=255,default="")
    name = models.CharField(max_length=255,default="")
    
    def __Str__(self):
        return self.id


class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=255,default="")
    delivered = models.IntegerField(default=0)
    total_emails = models.IntegerField(default=0)
    clicked = models.IntegerField(default=0)
    opened = models.IntegerField(default=0)
    invalid = models.IntegerField(default=0)
    unsubscribed = models.IntegerField(default=0)
    bounced = models.IntegerField(default=0)
    sent_emails = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_sent = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=100,default="Not yet started")
    client = models.CharField(max_length=100)
    clist = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    replyTo = models.CharField(max_length=255)
    redirect_urls = models.CharField(max_length=300)
    time_delta = models.IntegerField(default=1)
    
    def __Str__(self):
        return self.id


class MessageInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    message_id = models.CharField(max_length=100,default="")
    thread_id = models.CharField(max_length=100,default="")
    unsubscribe = models.CharField(max_length=3,default="no")
    sent = models.BooleanField(default=False)
    bounced = models.CharField(max_length=3,default="no")
    invalid = models.CharField(max_length=3,default="no")
    clicks = models.IntegerField(default=0)
    opens = models.IntegerField(default=0)
    sent_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __Str__(self):
        return self.id