from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from rest_framework import status, views, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Template, Campaign
from .serializers import getTemplateSerializer, getTemplateListSerializer, getcampaignSerializer
from rest_framework import generics
from contacts.models import contactList

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter
import pytz
from pprint import pprint
from datetime import datetime, timezone

from .common_functions import (check_unsubscribe,
                                         process_click_links, process_open_id)

from .task import Send_Emails
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

class getTemplateListView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        queryset = Template.objects.filter(user=request.user)
        serializer = getTemplateListSerializer(queryset,many=True)
        return Response(serializer.data)

class getTemplatedataView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self,request,pk):
        obj = Template.objects.get(id=pk)
        if request.user == obj.user:
            data = {'message': "","subject":obj.subject}
            with open(obj.message,'r') as f:
                data['message'] = f.read()
            return Response(data)
        else:
            return Response(status=409)

class getTimezonesView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        data = pytz.all_timezones
        return Response(data)



class createCampaignView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self,request):
        data = request.data
        if len(Campaign.objects.filter(campaign_name=data['name']).filter(user=request.user)) != 0:
            return Response(status=409)
        obj = contactList.objects.get(id = int(data['selectedList']))
        clist = []
        for i in obj.contact.all():
            clist.append(str(i.id))
        clist = "|".join(clist)
        with open(f"media/temData/{request.user.username}_{data['name']}_clist.txt","w") as f:
            f.write(clist)
        with open(f"media/temData/{request.user.username}_{data['name']}_message.txt","w") as f:
            f.write(data["message"])
        with open(f"media/temData/{request.user.username}_{data['name']}_urls.txt","w") as f:
            f.write("")
        camp_obj = Campaign.objects.create(
            user = request.user,
            campaign_name = data['name'],
            client = data['client'],
            clist = f"media/temData/{request.user.username}_{data['name']}_clist.txt",
            message = f"media/temData/{request.user.username}_{data['name']}_message.txt",
            subject = data['subject'],
            display = data['display_name'],
            replyTo = data['reply_to'],
            redirect_urls = f"media/temData/{request.user.username}_{data['name']}_urls.txt",
            time_delta = int(data["time_delta"])
        )
            
        timezone_info = data["tzone"]
        date = data["date"].split("-")
        time = data["time"].split(":")
        date_object = datetime.now(tz=pytz.timezone(timezone_info))
        date_object = date_object.replace(minute=int(time[1]), hour=int(time[0]), year=int(date[0]), month=int(date[1]), day=int(date[2]))
        if "UTC" != timezone_info:
            date_object = date_object.replace(tzinfo=pytz.timezone(timezone_info)).astimezone(tz=pytz.timezone("UTC"))
        
        Send_Emails.apply_async(
            eta = date_object,
            kwargs = {
                'campaign_id':camp_obj.id
                }
            )
        return Response(status=200)


# sunsubscription handler
def getUnSubscriptions(request,pk_1,pk_2):
    if request.method == "GET":
        check_unsubscribe(int(pk_1),int(pk_2))
    return render(request,"unsubscribe.html")

# clicked links handler
def getClicks(request,pk_1,pk_2,pk_3):
    if request.method == "GET":
        link = process_click_links(int(pk_1),int(pk_2),int(pk_3))
    return redirect(link)

# opened emails handler
def getOpens(request,pk_1,pk_2):
    if request.method == "GET":
        process_open_id(int(pk_1),int(pk_2))
    return HttpResponse("")


class campaignTable(generics.ListAPIView):
    serializer_class = getcampaignSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_classes = LimitOffsetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('campaign_name', 'client', 'subject', 'display', 'replyTo', 'created', 'last_sent', 'status')
    ordering_fields = ('campaign_name', 'created')

    def get_queryset(self):
        """
        restricts the returned contacts to a given user
        """
        queryset = Campaign.objects.filter(user=self.request.user)
        return queryset



class deleteCampaignView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def destroy(self,request,pk):
        Campaign.objects.get(id=pk).delete()
        return Response('success')