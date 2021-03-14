from django.urls import path, re_path
from .views import getToekenViewset, BulkUserDeleteViewset
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'manage',getToekenViewset,basename='manageContact')
router.register(r'bulk/delete',BulkUserDeleteViewset,basename='bulkDeleteContacts')

app_name = 'user'

urlpatterns = [
]

urlpatterns += router.urls