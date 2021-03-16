from django.urls import path, re_path
from .views import getTemplateView, getTemplateMessageView
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'template/manage',getTemplateView,basename='manageTemplate')
router.register(r'template/get/message',getTemplateMessageView,basename='getTemplateMessage')

app_name = 'campaigns'

urlpatterns = [
]

urlpatterns += router.urls