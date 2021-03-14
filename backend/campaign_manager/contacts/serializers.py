from rest_framework import serializers

from .models import Contact

# write your serializers bellow

class getContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','first_name','last_name','email','mobile','address','bank','ref','desc')