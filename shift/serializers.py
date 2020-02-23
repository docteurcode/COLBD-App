from rest_framework import serializers

from .models import ConnectionShift


class ConnectionShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionShift
        fields = ['is_done', 'distic', 'thana', 'address']
        
