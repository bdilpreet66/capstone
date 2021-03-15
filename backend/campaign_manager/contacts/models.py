from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,default="")
    last_name = models.CharField(max_length=255,default="")
    email = models.CharField(max_length=255,default="")
    mobile = models.CharField(max_length=255,default="")
    address = models.CharField(max_length=255,default="")
    bank = models.CharField(max_length=255,default="")
    ref = models.CharField(max_length=255,default="")
    desc = models.CharField(max_length=255,default="")
    
    def __Str__(self):
        return self.id

class contactList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ManyToManyField(Contact, blank=True)
    name = models.CharField(max_length=255,default="")
    ref = models.CharField(max_length=255,default="")
    description = models.CharField(max_length=255,default="")
    
    def __Str__(self):
        return self.id