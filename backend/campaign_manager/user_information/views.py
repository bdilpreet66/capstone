from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# from user.confirmation_token import account_activation_token

from .models import Profile, Gmail
from .serializers import (CreateUserSerializer, GetUserSerailizer, getUserTokenSerializer)
from .gmail_client import get_cred_from_token, get_auth_url
import pickle
# Create your views here.



class getToekenViewset(viewsets.ViewSet):
    def create(self,request):
        data = request.data
        user = authenticate(username=data["username"], password=data["password"])
        queryset = Token.objects.get(user=user)
        try:
            if user is not None:
                serializer = getUserTokenSerializer(queryset, many=False)
                return Response(serializer.data)
            else:
                return Response(status_code=404)
        except:
            return Response(status_code=404)


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class SignInViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        user=request.user
        profile = Profile.objects.get(user=user)
        serializer = GetUserSerailizer(profile,many=False)
        return Response(serializer.data)


class ChangePPicViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        profile = Profile.objects.get(user=request.user)
        profile.logo = request.data['file']
        profile.save()
        return Response({'data':str(profile.logo)},status=200)


class updateProfileViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        data = request.data
        profile = Profile.objects.get(user=request.user)
        profile.company_site = data['website']
        profile.contact_number = data['mob']
        profile.company_name = data['cname']
        request.user.first_name = data['fname']
        request.user.last_name = data['lname']
        request.user.email = data['email']
        profile.save()
        request.user.save()
        return Response(data,status=200)


class updatePasswordViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        data = request.data
        if request.user.check_password(data['cpass']):
            request.user.set_password(data['pass'])
            request.user.save()
            return Response(status=200)
        else:
            return Response(status=404)

class getGoogleCredentialsViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        url = get_auth_url()
        return Response(url)

    def create(self,request):
        
        creds,email = get_cred_from_token(request.data["code"])
        obj = Gmail.objects.filter(user=request.user)
        if len(obj) == 0:
            obj = Gmail.objects.create(
                user = request.user,
                email = "",
                key = ""
            )
        else:
            obj=obj[0]
        file_name = f"media/token_gmail_{request.user.id}.pickle"
        with open(file_name, 'wb') as token:
            pickle.dump(creds, token)
        obj.key = file_name
        obj.active = True
        obj.email = email
        obj.save()
        return Response("SUCCESS")

class DisconnectGoogleViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        
        user = request.user
        client_obj = Gmail.objects.get(user=user)
        client_obj.active =False
        client_obj.save()

        return Response(data)