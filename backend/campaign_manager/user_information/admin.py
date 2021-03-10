from django.contrib import admin
from .models import Team, Profile, Package
# Register your models here.

admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Package)