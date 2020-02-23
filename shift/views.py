from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ConnectionShiftSerializer
from .models import ConnectionShift
# Create your views here.


class ConnectionShiftViewApi(viewsets.ModelViewSet):
    serializer_class = ConnectionShiftSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    queryset = ConnectionShift.objects.all()
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
