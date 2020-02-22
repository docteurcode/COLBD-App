from django.shortcuts import render
from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .serializers import UserInfoSerializer, UserDetailsSerializer, UserSerializer, AuthTokenSerializer, InfoSerializer
from .models import Info

# Create your views here.


class UserInfoApiView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = UserInfoSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self, ):
        if self.action == 'retrieve':
            return UserDetailsSerializer

        return self.serializer_class

# Login stuff


class CreateUserApi(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserViewApi(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class CreateInfoApi(generics.CreateAPIView):
    serializer_class = InfoSerializer


class InfoViewApi(viewsets.ReadOnlyModelViewSet):
    serializer_class = InfoSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    queryset = Info.objects.all()

    # def get_object(self):
    #     return self.request.user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AuthTokenApi(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
