from django.urls import path, re_path
from .views import SignUpViewSet, SignInViewSet, getToekenViewset, ChangePPicViewSet, updateProfileViewSet, updatePasswordViewSet, getGoogleCredentialsViewSet, DisconnectGoogleViewSet
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
router.register(r'google/disconnect',DisconnectGoogleViewSet,basename='disconnect_from_google')

app_name = 'user'

urlpatterns = [
]

urlpatterns += router.urls
