from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from Account.models import User
from .models import NormalProfile, FollowersFollowing


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        NormalProfile.objects.create(
            user=instance,
            name=instance.full_name,
            profile_pick='/Default/Profile_icon.svg'
        )

        FollowersFollowing.objects.create(
            following_user=instance,
        )

