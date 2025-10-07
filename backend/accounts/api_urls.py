from django.urls import path
from accounts.api_views import SignupAPI, UserDetailAPI, CustomObtainAuthToken

urlpatterns = [
    path('signup/', SignupAPI.as_view(), name='api-signup'),
    path('login/', CustomObtainAuthToken.as_view(), name='api-login'),
    path('me/', UserDetailAPI.as_view(), name='api-me'),
]
