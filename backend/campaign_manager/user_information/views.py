from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# from user.confirmation_token import account_activation_token

from .models import Profile, Gmail, Custom, Outlook
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

class ConnectOutlookViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        data = request.data
        obj = Outlook.objects.filter(user=request.user)
        if len(obj) == 0:
            obj = Outlook.objects.create(
                user = request.user,
                email = data['email'],
                username = data['username'],
                IMAP_password = data['IMAP_password'],
                IMAP_host = data['IMAP_host'],
                IMAP_type = data['IMAP_type'],
                IMAP_port = data['IMAP_port'],
                smtp_host = data['smtp_host'],
                smtp_port = data['smtp_port'],
                smtp_password = data['smtp_password'],
                smtp_type = data['smtp_type'],
                emails_per_day = data['emails_per_day'],
                daily_limit_left = data['emails_per_day'],
                active = True
            )
        else:
            obj = obj[0]
            obj.email = data['email']
            obj.username = data['username']
            obj.IMAP_password = data['IMAP_password']
            obj.IMAP_host = data['IMAP_host']
            obj.IMAP_type = data['IMAP_type']
            obj.IMAP_port = data['IMAP_port']
            obj.smtp_host = data['smtp_host']
            obj.smtp_port = data['smtp_port']
            obj.smtp_password = data['smtp_password']
            obj.smtp_type = data['smtp_type']
            obj.emails_per_day = data['emails_per_day']
            obj.daily_limit_left = data['emails_per_day']
            obj.active = True
            obj.save()
        return Response("SUCCESS")

class ConnectCustomViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        data = request.data
        obj = Custom.objects.filter(user=request.user)
        if len(obj) == 0:
            obj = Custom.objects.create(
                user = request.user,
                smtpemail = data['SMTPemail'],
                imapemail = data['IMAPemail'],
                smtpusername = data['SMTPusername'],
                imapusername = data['IMAPusername'],
                IMAP_password = data['IMAP_password'],
                IMAP_host = data['IMAP_host'],
                IMAP_type = data['IMAP_type'],
                IMAP_port = data['IMAP_port'],
                smtp_host = data['smtp_host'],
                smtp_port = data['smtp_port'],
                smtp_password = data['smtp_password'],
                smtp_type = data['smtp_type'],
                emails_per_day = data['emails_per_day'],
                daily_limit_left = data['emails_per_day'],
                active = True
            )
        else:
            obj = obj[0]
            obj.smtpemail = data['SMTPemail']
            obj.imapemail = data['IMAPemail']
            obj.smtpusername = data['SMTPusername']
            obj.imapusername = data['IMAPusername']
            obj.IMAP_password = data['IMAP_password']
            obj.IMAP_host = data['IMAP_host']
            obj.IMAP_type = data['IMAP_type']
            obj.IMAP_port = data['IMAP_port']
            obj.smtp_host = data['smtp_host']
            obj.smtp_port = data['smtp_port']
            obj.smtp_password = data['smtp_password']
            obj.smtp_type = data['smtp_type']
            obj.emails_per_day = data['emails_per_day']
            obj.daily_limit_left = data['emails_per_day']
            obj.active = True
            obj.save()
        print(obj.active)
        return Response("SUCCESS")

class DisconnectGoogleViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        
        user = request.user
        client_obj = Gmail.objects.get(user=user)
        client_obj.active =False
        client_obj.save()

        return Response("success")

class DisconnectOutlookViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        
        user = request.user
        client_obj = Outlook.objects.get(user=user)
        client_obj.active = False
        client_obj.save()

        return Response("success")

class DisconnectCustomViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        
        user = request.user
        client_obj = Custom.objects.get(user=user)
        client_obj.active = False
        client_obj.save()

        return Response("success")

class ActiveClientsViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        data = {
            'custom':False,
            'gmail':False,
            'outlook':False,
        }
        user = request.user
        try:
            obj = Custom.objects.filter(user=user)
            data['custom'] = obj[0].active
        except:
            pass
        try:
            obj = Outlook.objects.filter(user=user)
            data['outlook'] = obj[0].active
        except:
            pass
        try:
            obj = Gmail.objects.filter(user=user)
            data['gmail'] = obj[0].active
        except:
            pass
        return Response(data)