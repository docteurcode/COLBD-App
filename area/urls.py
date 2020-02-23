from django.urls import path

from .views import ThanaApiView, DisticApiView

urlpatterns = [
    path('thana', ThanaApiView.as_view(), name='thana'),
    path('distic', DisticApiView.as_view(), name='distic'),
]
