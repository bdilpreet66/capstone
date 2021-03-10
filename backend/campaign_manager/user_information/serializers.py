from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Team, Profile, Package

# write your serializers bellow

class GetUserSerailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

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
            is_active = False
        )
        obj.set_password(validated_data['password'])
        obj.save()
        package = Package.objects.create()
        myteam = Team.objects.create(user=obj,package=package)
        Token.objects.create(user=obj)
        Profile.objects.create(user=obj)
        return obj
