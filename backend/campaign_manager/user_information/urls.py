from django.urls import path, re_path
from .views import SignUpViewSet, SignInViewSet
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'account/signup',SignUpViewSet,basename='signup')
router.register(r'account/get_info',SignInViewSet,basename='basic_profile_info')

app_name = 'user'

urlpatterns = [
]

urlpatterns += router.urls