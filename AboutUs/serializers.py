from rest_framework import serializers
from .models import AboutUs

# Indicating Proper Image Path
from django.conf import settings
urlPath = settings.IMAGE_STORE_AT


class AboutUsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = AboutUs
        fields = ['name', 'role', 'details', 'image_url', 'time_stamp']

    def get_image_url(self, obj):
        return str(urlPath[0]) + obj.image.url

