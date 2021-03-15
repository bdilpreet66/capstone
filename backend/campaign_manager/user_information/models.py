from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


        
class Package(models.Model):
    package_types = [
                    ('T', 'Trail'),
                    ('M', 'Monthly'),
                    ('D', 'Daily'),
                    ('Y', 'Yearly'),
                    ('M6', '6_Month'),
                    ('M3', '3_Month'),
                ]
    package_duration = models.CharField(
                            max_length=2,
                            choices=package_types,
                            default='T',
                        )
    start_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    end_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __Str__(self):
        return self.id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pic = some_field
    country = models.CharField(max_length=255,default="")
    contact_number = models.CharField(max_length=255)
    position=models.CharField(max_length=255,default="manager")
    company_name = models.CharField(max_length = 255, null = True, blank = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __Str__(self):
        return self.id

class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    package = models.OneToOneField(Package, on_delete=models.CASCADE)
    is_trail = models.BooleanField(default=True)
    
    def __Str__(self):
        return self.id