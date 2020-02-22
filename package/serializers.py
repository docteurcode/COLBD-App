from rest_framework import serializers

from .models import Package, PackageOffer


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'speed', 'price']
        read_only_fields = ['id', ]


class PackageDetailsSerializer(serializers.ModelSerializer):
    bdix = serializers.CharField(source='get_bdix_display')
    youtube = serializers.CharField(source='get_youtube_display')
    ftp = serializers.CharField(source='get_ftp_display')
    ftp = serializers.CharField(source='get_ftp_display')
    facebook = serializers.CharField(source='get_facebook_display')

    class Meta:
        model = Package
        exclude = ['id', 'created_at', 'updated_at', 'is_pub']


class PackageOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageOffer
        fields = ['month', 'installation_charge']
