from django.db import models
from django.contrib.auth.models import User


class Template(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255,default="")
    subject = models.CharField(max_length=255,default="")
    name = models.CharField(max_length=255,default="")
    
    def __Str__(self):
        return self.id
