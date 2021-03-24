from django.urls import path, re_path
from .views import ActiveClientsViewSet, DisconnectCustomViewSet, DisconnectOutlookViewSet, SignUpViewSet, SignInViewSet, getToekenViewset, ChangePPicViewSet, updateProfileViewSet, updatePasswordViewSet, getGoogleCredentialsViewSet, DisconnectGoogleViewSet, ConnectOutlookViewSet, ConnectCustomViewSet
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'account/signup',SignUpViewSet,basename='signup')
router.register(r'account/login',getToekenViewset,basename='login')
router.register(r'account/get_info',SignInViewSet,basename='basic_profile_info')
router.register(r'update/ppic',ChangePPicViewSet,basename='ppic_update')
router.register(r'update/profile',updateProfileViewSet,basename='profile_update')
router.register(r'update/password',updatePasswordViewSet,basename='password_update')
router.register(r'google/connect',getGoogleCredentialsViewSet,basename='connect_to_google')
router.register(r'outlook/connect',ConnectOutlookViewSet,basename='connect_to_outlook')
router.register(r'custom/connect',ConnectCustomViewSet,basename='connect_to_custom')
router.register(r'google/disconnect',DisconnectGoogleViewSet,basename='disconnect_from_google')
router.register(r'outlook/disconnect',DisconnectOutlookViewSet,basename='disconnect_from_outlook')
router.register(r'custom/disconnect',DisconnectCustomViewSet,basename='disconnect_from_custom')
router.register(r'get/active/clients',ActiveClientsViewSet,basename='disconnect_from_custom')

app_name = 'user'

urlpatterns = [
]

urlpatterns += router.urls
