from django.contrib.auth.models import User
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Template
from .serializers import getTemplateSerializer
from rest_framework import generics

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.

class getTemplateView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        queryset = Template.objects.filter(user=request.user)
        serializer = getTemplateSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        data = request.data
        user = request.user
        tname = f"media/templates/" + data['name'] + f"{user.id}.txt"
        obj = Template.objects.create(
            user = user,
            message = tname,
            name = data['name'],
            subject = data['subject']
        )
        with open(tname,'w') as f:
            f.write(data['message'])
        serializer = getTemplateSerializer(obj,many=False)
        return Response(serializer.data)

    def update(self,request,pk):
        data = request.data
        obj = Template.objects.get(id=pk)
        if obj.user == request.user:
            obj.subject = data['subject']
            obj.name = data['name']
        obj.save()
        with open(obj.message,'w') as f:
            f.write(data['message'])
        serializer = getTemplateSerializer(obj,many=False)
        return Response(serializer.data)

    def destroy(self,request,pk):
        Template.objects.get(id=pk).delete()
        return Response('success')

class getTemplateMessageView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self,request,pk):
        obj = Template.objects.get(id=pk)
        with open(obj.message,'r') as f:
            data = {'message': f.read()}
        return Response(data)


class TemplateTable(generics.ListAPIView):
    serializer_class = getTemplateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_classes = LimitOffsetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', 'subject')
    ordering_fields = ('name')

    def get_queryset(self):
        """
        restricts the returned contacts to a given user
        """
        queryset = Template.objects.filter(user=self.request.user)
        return queryset