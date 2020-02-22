from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from .models import Info


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'col_id', 'status', 'package', 'expired_at']
        read_only_fields = ['id', ]


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        read_only_fields = ['id', 'col_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ['col_id', 'status']
        fields = ['username', 'email', 'password']
        extra_kwargs = {"password": {
            'write_only': True, 'min_length': 5, 'max_length': 5}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class InfoSerializer(serializers.ModelSerializer):
    distic = serializers.SlugRelatedField(read_only=True, slug_field='name')
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    thana = serializers.SlugRelatedField(read_only=True, slug_field='name')
    package = serializers.SlugRelatedField(
        read_only=True, slug_field='name')  # we r going to use hyperlink
    # status = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # status = serializers.SerializerMethodField()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Info
        # exclude = ['status', ]
        fields = '__all__'
        # depth = 1


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(
        style={'input_type': "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(request=self.context.get(
            'request'), username=username, password=password)
        if not user:
            msg = _('Please check your username and password')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
