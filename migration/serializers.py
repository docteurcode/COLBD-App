from rest_framework import serializers

from .models import Migrate


class MigrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Migrate
        # fields = '__all__'
        exclude = ['user', ]
        read_only_fields = ['id', ]
