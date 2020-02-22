from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
# from rest_framework.filters import SearchFilter

from .serializers import PackageOfferSerializer, PackageSerializer, PackageDetailsSerializer
from .models import Package, PackageOffer
# Create your views here.


class PackageApiView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.filter(is_pub=True).all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PackageDetailsSerializer
        return PackageSerializer


class PackageOfferApiView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PackageOfferSerializer
    queryset = PackageOffer.objects.all()

    def get_queryset(self):
        package = self.request.query_params.get('package', None)
        if package:
            return self.queryset.filter(package__id=package)
        return {}
