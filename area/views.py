from django.shortcuts import render
from rest_framework import generics

from .models import Distic, Thana
from .serializers import DisticSerializer, ThanaSerializer
# Create your views here.


class ThanaApiView(generics.ListAPIView):
    serializer_class = ThanaSerializer
    queryset = Thana.objects.all()


class DisticApiView(generics.ListAPIView):
    serializer_class = DisticSerializer
    queryset = Distic.objects.all()
