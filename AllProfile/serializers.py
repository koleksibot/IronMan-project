from rest_framework import serializers
from Account.models import User
from .models import NormalProfile, FollowersFollowing
from Account.serializers import UserSerializer

# Indicating Proper Image Path
from django.conf import settings
urlPath = settings.IMAGE_STORE_AT


class NormalProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    profile_picture = serializers.ImageField(read_only=True)
    profile_picture_id = serializers.IntegerField(
        write_only=True, required=False)

    class Meta:
        model = NormalProfile
        fields = "__all__"


class NormalProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = NormalProfile
        fields = ['name', 'age', 'address', 'status', 'phone_no', 'description', 'gender']


class FollowersFollowingSerializer(serializers.ModelSerializer):
    normalprofile = serializers.SerializerMethodField('get_normalprofile')
    is_following = serializers.SerializerMethodField('get_is_following')

    class Meta:
        model = FollowersFollowing
        fields = [
            'id',
            'normalprofile',
            'following_user',
            'get_total_followers',
            'get_total_following',
            'is_following',
        ]
        read_only_fields = ['get_total_following', 'get_total_followers']

    def get_normalprofile(self, obj):
        user = User.objects.get(id=obj.id)
        img_url = str(urlPath[0]) + user.normalprofile.profile_pick.url
        full_name = user.normalprofile.name
        gender = user.normalprofile.gender
        address = user.normalprofile.address
        status = user.normalprofile.status
        description = user.normalprofile.description
        age = user.normalprofile.age
        return {
            'img_url': img_url,
            'name': full_name,
            'status': status,
            'gender': gender,
            'age': age,
            'more_info': description,
            'address': address,
        }

    def get_is_following(self, obj):
        followed_by = User.objects.get(id=self.context['request'].user.pk)
        following_user = User.objects.get(id=obj.id)
        following = FollowersFollowing.objects.filter(following_user=following_user, followed_by=followed_by)
        if following:
            return True
        else:
            return False


class FollowersFollowingListSerializer(serializers.ModelSerializer):
    normalprofile = serializers.SerializerMethodField('get_normalprofile')
    is_following = serializers.SerializerMethodField('get_is_following')

    class Meta:
        model = FollowersFollowing
        fields = [
            'id',
            'normalprofile',
            'following_user',
            'get_total_followers',
            'get_total_following',
            'is_following',
        ]
        read_only_fields = ['get_total_following', 'get_total_followers']

    def get_normalprofile(self, obj):
        user = User.objects.get(id=obj.id)
        img_url = str(urlPath[0]) + user.normalprofile.profile_pick.url
        full_name = user.normalprofile.name
        gender = user.normalprofile.gender
        address = user.normalprofile.address
        description = user.normalprofile.description
        return {
            'img_url': img_url,
            'name': full_name,
            'gender': gender,
            'address': address,
            'more_info': description,
        }

    def get_is_following(self, obj):
        followed_by = User.objects.get(id=self.context['request'].user.pk)
        following_user = User.objects.get(id=obj.id)
        following = FollowersFollowing.objects.filter(following_user=following_user, followed_by=followed_by)
        if following:
            return True
        else:
            return False

