from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Contact
from .serializers import getContactSerializer

# Create your views here.

class getToekenViewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        queryset = Contact.objects.filter(user=request.user)
        serializer = getContactSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        data = request.data
        user = request.user
        obj = Contact.objects.create(
            user = user,
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            mobile = data['mobile'],
            address = data['address'],
            bank = data['bank'],
            ref = data['ref'],
            desc = data['desc']
        )
        serializer = getContactSerializer(obj,many=False)
        return Response(serializer.data)

    def update(self,request,pk):
        data = request.data
        obj = Contact.objects.get(id=pk)
        if obj.user == request.user:
            obj.first_name = data['first_name'],
            obj.last_name = data['last_name'],
            obj.email = data['email'],
            obj.mobile = data['mobile'],
            obj.address = data['address'],
            obj.bank = data['bank'],
            obj.ref = data['ref'],
            obj.desc = data['desc']
        obj.save()
        serializer = getContactSerializer(obj,many=False)
        return Response(serializer.data)

    def destroy(self,request,pk):
        Contact.objects.get(id=pk).delete()
        return Response('success')


class BulkUserDeleteViewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        data = request.data
        for i in data['blukList']:
            Contact.objects.get(id=i).delete()
        return Response('success')
