from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated

# from user.confirmation_token import account_activation_token

from .models import Profile, Team
from .serializers import (CreateUserSerializer, GetUserSerailizer)

# Create your views here.



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

