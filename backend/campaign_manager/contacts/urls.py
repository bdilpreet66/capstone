from django.urls import path, re_path
from .views import getContactViewset, BulkUserDeleteViewset, getContactListViewset
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'manage',getContactViewset,basename='manageContact')
router.register(r'bulk/delete',BulkUserDeleteViewset,basename='bulkDeleteContacts')
router.register(r'list',getContactListViewset,basename='manageList')

app_name = 'user'

urlpatterns = [
]

urlpatterns += router.urls