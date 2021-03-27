from rest_framework import serializers

from .models import Template, Campaign

# write your serializers bellow

class getTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id','name','subject')

class getTemplateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id','name')

class getcampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id','campaign_name', 'client', 'subject', 'display', 'replyTo', 'created', 'last_sent', 'status')