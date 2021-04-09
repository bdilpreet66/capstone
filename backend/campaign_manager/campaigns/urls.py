from django.urls import path, re_path
from .views import deleteCampaignView, campaignTable, getUnSubscriptions, getClicks, getOpens, createCampaignView, getTemplateView, getTemplateMessageView, TemplateTable, getTemplateListView, getTemplatedataView, getTimezonesView
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'template/list',getTemplateListView,basename='listTemplate')
router.register(r'get/templateData',getTemplatedataView,basename='getTemplatedata')
router.register(r'template/manage',getTemplateView,basename='manageTemplate')
router.register(r'template/get/message',getTemplateMessageView,basename='getTemplateMessage')
router.register(r'get/timezone',getTimezonesView,basename='getTimezone')
router.register(r'create',createCampaignView,basename='createCampaign')
router.register(r'delete',deleteCampaignView,basename='deleteCampaign')

app_name = 'campaigns'

urlpatterns = [
    path('listTemplates',TemplateTable.as_view(), name="TemplateTable"),
    path('get',campaignTable.as_view(), name="TemplateTable"),
    # unsubscription handler
    re_path(r'unsub_email/(?P<pk_1>\d+)/(?P<pk_2>\d+)/',getUnSubscriptions, name="unsubscribe"),
    # clicked link handler
    re_path(r'click/(?P<pk_1>\d+)/(?P<pk_2>\d+)/(?P<pk_3>\d+)/',getClicks, name="clicks"),
    # opened emails handler
    re_path(r'open/(?P<pk_1>\d+)/(?P<pk_2>\d+)/',getOpens, name="opens"),
]

urlpatterns += router.urls