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