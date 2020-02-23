from rest_framework import serializers

from .models import Distic, Thana


class ThanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thana
        fields = ['name', ]


class DisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distic
        fields = ['name', ]
