from django.urls import path
from accounts.api_views import SignupAPI, CustomObtainAuthToken

urlpatterns = [
    path('signup/', SignupAPI.as_view(), name='api-signup'),
    path('login/', CustomObtainAuthToken.as_view(), name='api-login'),
]
