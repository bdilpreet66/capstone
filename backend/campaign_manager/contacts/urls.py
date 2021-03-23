from django.urls import path, re_path
from .views import getContactViewset, BulkUserDeleteViewset, getContactListViewset, ContactTable, ContactListTable, CreateListViewSet
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'manage',getContactViewset,basename='manageContact')
router.register(r'bulk/delete',BulkUserDeleteViewset,basename='bulkDeleteContacts')
router.register(r'list',getContactListViewset,basename='manageList')
router.register(r'Createlist',CreateListViewSet,basename='createList')

app_name = 'contacts'

urlpatterns = [
    path('listContacts',ContactTable.as_view(), name="listContact"),
    path('list/listTable',ContactListTable.as_view(), name="ContactlistTable"),
]

urlpatterns += router.urls