from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Profile

# write your serializers bellow

class getUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class getUserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class GetUserSerailizer(serializers.ModelSerializer):
    user = getUserInfoSerializer(read_only=True,many=False)
    class Meta:
        model = Profile
        fields = ('user','logo','company_site','contact_number','company_name')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {
            'password' : {'write_only': True,'required':True},
            'email' : {'required':True}
        }

    def create(self, validated_data):
        obj = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            is_superuser = False,
            is_staff = False,
            is_active = True
        )
        obj.set_password(validated_data['password'])
        obj.save()
        Token.objects.create(user=obj)
        Profile.objects.create(user=obj)
        return obj
