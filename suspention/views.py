from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import SuspentionPermanently, SuspentionTemporary
from .serializers import PermanentSuspentionSerializer, TemporarySuspentionSerializer
# Create your views here.


class PermanentSuspentionApiView(viewsets.ModelViewSet):
    serializer_class = PermanentSuspentionSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']
    queryset = SuspentionPermanently.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TemporarySuspentionApiView(viewsets.ModelViewSet):
    serializer_class = TemporarySuspentionSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']
    queryset = SuspentionTemporary.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
