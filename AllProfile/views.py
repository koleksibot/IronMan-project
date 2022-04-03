from django.shortcuts import render
from Account.models import User
from Account.serializers import UserSerializer

# Import From Models
from .models import NormalProfile, FollowersFollowing

# Import From Serializer
from .serializers import FollowersFollowingSerializer, FollowersFollowingListSerializer, NormalProfileUpdateSerializer

# For Authentication Purpose
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response

from collections import namedtuple
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profileDetail(request, pk):
    profile_details = FollowersFollowing.objects.get(id=pk)
    serializer = FollowersFollowingSerializer(profile_details, context={'request': request}, many=False)
    return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
def profileUpdate(request):
    """ This is Update Function For User Normal Profile """
    user = request.user
    print(user)
    try:
        normalprofile = NormalProfile.objects.get(user=request.user)
        print(normalprofile)
    except NormalProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NormalProfileUpdateSerializer(normalprofile, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Your Profile Is Update Success fully"
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list(request):
    followers_list = FollowersFollowing.objects.all()
    serializers = FollowersFollowingListSerializer(followers_list, context={'request': request}, many=True)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers_list(request):
    main_user = request.user
    users = User.objects.all().order_by('-id')
    followers = {}
    all_followers = []
    for f_user in users:
        is_followers = FollowersFollowing.objects.filter(followed_by=f_user, following_user=main_user)
        if is_followers:
            follower_user = FollowersFollowing.objects.filter(following_user=f_user)
            serializer = FollowersFollowingListSerializer(follower_user, context={'request': request}, many=True)
            all_followers.append(serializer.data)
    followers['followers'] = all_followers
    return Response(followers)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def following_list(request):
    main_user = request.user
    following_user = FollowersFollowing.objects.filter(followed_by=main_user)
    serializers = FollowersFollowingListSerializer(following_user, context={'request': request}, many=True)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_follow_un_follow(request, pk):
    """
    ~~~~~~~~~: To Follow & Un-Follow an User We Use This Code :~~~~~~~~~
    """
    following_user = User.objects.get(pk=pk)
    followed_by = request.user
    if following_user != followed_by:
        follow = FollowersFollowing.objects.filter(following_user=following_user, followed_by=followed_by)
        if follow:
            FollowersFollowing.un_follow(following_user, followed_by)
            return Response(False)
        else:
            FollowersFollowing.follow(following_user, followed_by)
            return Response(True)
    else:
        return Response({'is_follow': 'False'})

