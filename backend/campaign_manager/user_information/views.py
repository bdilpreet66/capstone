from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# from user.confirmation_token import account_activation_token

from .models import Profile, Team
from .serializers import (CreateUserSerializer, GetUserSerailizer, getUserTokenSerializer)

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
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        user=request.user
        serializer = GetUserSerailizer(user,many=False)
        return Response(serializer.data)

