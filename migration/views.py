from django.shortcuts import render
from rest_framework import status, viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Migrate
from .serializers import MigrationSerializer
from rest_framework.response import Response
# Create your views here.


class MigrateApiView(viewsets.ModelViewSet):
    serializer_class = MigrationSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Migrate.objects.all()
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
