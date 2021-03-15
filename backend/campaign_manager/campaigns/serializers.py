from rest_framework import serializers

from .models import Template

# write your serializers bellow

class getTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id','name','subject')