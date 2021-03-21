from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Contact, contactList
from .serializers import getContactSerializer, getContactListSerializer
from rest_framework import generics

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.

class ContactTable(generics.ListAPIView):
    serializer_class = getContactSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_classes = LimitOffsetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('address', 'bank', 'desc', 'email', 'first_name', 'last_name', 'mobile', 'ref')
    ordering_fields = ('first_name', 'last_name','email')

    def get_queryset(self):
        """
        restricts the returned contacts to a given user
        """
        queryset = Contact.objects.filter(user=self.request.user)
        return queryset

class getContactViewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        queryset = Contact.objects.filter(user=request.user)[:10]
        serializer = getContactSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        data = request.data
        user = request.user
        obj = Contact.objects.filter(ref=data['ref'])
        if obj != []:
            return Response(status=409)
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
            obj.first_name = data['first_name']
            obj.last_name = data['last_name']
            obj.email = data['email']
            obj.mobile = data['mobile']
            obj.address = data['address']
            obj.bank = data['bank']
            obj.ref = data['ref']
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

class getContactListViewset(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        queryset = contactList.objects.filter(user=request.user)
        serializer = getContactListSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        data = request.data
        user = request.user
        obj = contactList.objects.filter(ref=data['ref'])
        if obj != []:
            return Response(status=409)
        obj = contactList.objects.create(
            user = user,
            name = data['name'],
            ref = data['ref'],
            description = data['description']
        )
        for i in data['lis']:
            obj.contact.add(Contact.objects.get(id=i))
        obj.save()
        serializer = getContactListSerializer(obj,many=False)
        return Response(serializer.data)

    def update(self,request,pk):
        data = request.data
        obj = contactList.objects.get(id=pk)
        if obj.user == request.user:
            name = data['name'],
            ref = data['ref'],
            description = data['description']
        for i in data['removelis']:
            obj.contact.remove(Contact.objects.get(id=i))
        for i in data['addlis']:
            obj.contact.add(Contact.objects.get(id=i))
        obj.save()
        serializer = getContactListSerializer(obj,many=False)
        return Response(serializer.data)

    def destroy(self,request,pk):
        contactList.objects.get(id=pk).delete()
        return Response('success')


class ContactListTable(generics.ListAPIView):
    serializer_class = getContactListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_classes = LimitOffsetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', 'ref', 'description')
    ordering_fields = ('name')

    def get_queryset(self):
        """
        restricts the returned contacts to a given user
        """
        queryset = contactList.objects.filter(user=self.request.user)
        return queryset