from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="images/logo", default="images/logo.png", blank=True)
    company_site = models.CharField(max_length=255,default="")
    contact_number = models.CharField(max_length=255)
    company_name = models.CharField(max_length = 255, null = True, blank = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __Str__(self):
        return self.id



class Gmail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    key = models.CharField(max_length=255,null=False, blank=False)
    emails_per_day = models.IntegerField(default=400)
    daily_limit_left = models.IntegerField(default=400)
    active = models.BooleanField(default=False)




class Outlook(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    username = models.CharField(max_length=255,blank=True,null=True)
    IMAP_password = models.CharField(max_length=255,blank=True,null=True)
    IMAP_host = models.CharField(max_length=255,blank=True,null=True)
    IMAP_type = models.CharField(max_length=255,default="Enable SSL")
    IMAP_port = models.IntegerField(blank=True,null=True)
    smtp_host = models.CharField(max_length=255,blank=True,null=True)
    smtp_port = models.IntegerField(blank=True,null=True)
    smtp_password = models.CharField(max_length=255,blank=True,null=True)
    smtp_type = models.CharField(max_length=255,default="STARTTLS")
    emails_per_day = models.IntegerField(default=500)
    daily_limit_left = models.IntegerField(default=-1)
    active = models.BooleanField(default=False)


class Custom(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    smtpemail = models.EmailField(null=False, blank=False)
    imapemail = models.EmailField(null=True, blank=True)
    smtpusername = models.CharField(max_length=255,blank=True,null=True)
    imapusername = models.CharField(max_length=255,blank=True,null=True)
    IMAP_password = models.CharField(max_length=255,blank=True,null=True)
    IMAP_host = models.CharField(max_length=255,blank=True,null=True)
    IMAP_type = models.CharField(max_length=255,default="Enable SSL")
    IMAP_port = models.IntegerField(blank=True,null=True)
    smtp_host = models.CharField(max_length=255,blank=True,null=True)
    smtp_port = models.IntegerField(blank=True,null=True)
    smtp_password = models.CharField(max_length=255,blank=True,null=True)
    smtp_type = models.CharField(max_length=255,default="STARTTLS")
    emails_per_day = models.IntegerField(default=500)
    daily_limit_left = models.IntegerField(default=-1)
    active = models.BooleanField(default=False)