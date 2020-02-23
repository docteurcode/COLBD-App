from rest_framework import serializers

from .models import SuspentionPermanently, SuspentionTemporary


class PermanentSuspentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspentionPermanently
        fields = ['is_done', 'device_collect_at', 'created_at']


class TemporarySuspentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuspentionTemporary
        fields = ['start_month', 'num_of_month', 'approve']
