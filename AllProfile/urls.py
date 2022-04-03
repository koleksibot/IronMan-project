from django.urls import path
from .views import (
    profileDetail,
    profileUpdate,
    users_list,
    user_follow_un_follow,
    followers_list,
    following_list,
)

urlpatterns = [
    path('profile_details/<int:pk>/', profileDetail, name="ProfileDetails"),
    path('profile_update/', profileUpdate, name="ProfileUpdate"),
    path('users_list/', users_list, name="AllUsersList"),
    path('follow_unfollow/<int:pk>/', user_follow_un_follow, name="Follow&UnFollow"),
    path('followers_list/', followers_list, name="FollowersList"),
    path('following_list/', following_list, name="FollowingList"),
]

