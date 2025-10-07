from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import UserCreateSerializer, UserSerializer


class SignupAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# optional: custom token view to return user data and token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=resp.data['token'])
        user = token.user
        return Response({'token': token.key, 'user': UserSerializer(user).data})