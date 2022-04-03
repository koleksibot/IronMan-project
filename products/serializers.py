from rest_framework import serializers

from Account.serializers import UserSerializer
from Account.models import User

from .models import Product

# Indicating Proper Image Path
from django.conf import settings
urlPath = settings.IMAGE_STORE_AT


class ProductsListSerializer(serializers.ModelSerializer):
    prod_picture_url = serializers.SerializerMethodField('get_prod_picture_url')
    prod_upload_by_user = serializers.SerializerMethodField('get_prod_upload_by')

    class Meta:
        model = Product
        fields = [
            'id',
            'prod_name',
            'prod_picture',
            'prod_picture_url',
            'prod_price',
            'quantity',
            'in_terms_of',
            'country_Of_Origin',
            'prod_description',
            'prod_offer',
            'creat_date',
            'prod_upload_by_user',

        ]
        read_only_fields = ['id', 'prod_picture_url',  'creat_date', 'prod_upload_by_user']

    def get_prod_picture_url(self, obj):
        picture_url = str(urlPath[0]) + obj.prod_picture.url
        return picture_url

    def get_prod_upload_by(self, obj):
        id = obj.prod_uploded_by.id
        prod_upload_by = obj.prod_uploded_by.name
        picture_url = str(urlPath[0]) + obj.prod_uploded_by.profile_pick.url
        return {
            'id': id,
            'user': prod_upload_by,
            'profile_pick': picture_url
        }

