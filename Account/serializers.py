from Account.models import User, UserOTP
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Indicating Proper Image Path
from django.conf import settings
urlPath = settings.IMAGE_STORE_AT

# from django.contrib import auth
# from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    """
    Registration Serializer
    """
    username = serializers.CharField(allow_blank=False, min_length=8, max_length=50, required=True)
    full_name = serializers.CharField(allow_blank=True, min_length=6, max_length=100, required=True)
    phone = serializers.CharField(allow_blank=True, allow_null=True, max_length=10, required=False)
    password = serializers.CharField(max_length=60, min_length=8, required=True)
    email = serializers.EmailField(
        max_length=60,
        validators=[UniqueValidator(queryset=User.object.all())],

    )

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            full_name=validated_data['full_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserOTPSerializers(serializers.ModelSerializer):
    """
    OTP validation serializer
    """
    class Meta:
        model = UserOTP
        fields = ['otp']


class ResetPasswordEmailSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=8, max_length=50, required=True)
    email = serializers.EmailField(min_length=10, required=True)

    class Meta:
        fields = ['username', 'email']


class UserPasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, required=True)
    password2 = serializers.CharField(max_length=60, min_length=8, required=True)
    otp = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['password', 'password2', 'otp']

