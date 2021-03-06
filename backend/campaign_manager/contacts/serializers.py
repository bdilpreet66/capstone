from rest_framework import serializers

from .models import Contact, contactList

# write your serializers bellow

class getContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','first_name','last_name','email','mobile','address','bank','ref','desc')

class getContactInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','first_name','last_name','ref','desc','email')

class getContactListSerializer(serializers.ModelSerializer):
    contact = getContactInfoSerializer(read_only=True,many=True)
    class Meta:
        model = contactList
        fields = ('id','description','name','ref','contact')