from django.db import models

# Create your models here.
from django.db import models
from Account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.timezone import now
from django.db.models import Q


# ______________________________________________________________________
#                  Normal Profile Section
# ______________________________________________________________________
class NormalProfile(models.Model):
    """
    This is "ALL USERS PROFILE" Model
    """
    name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    age = models.IntegerField(default=12, validators=[MinValueValidator(12)])
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="I use this app to help others...", null=True, blank=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],
                                max_length=15,
                                null=True,
                                blank=True
                                )
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    profile_pick = models.ImageField(upload_to='Other/Profile/images',
                                     null=True, blank=True,
                                     )
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = NormalProfile.objects.get(id=self.id)
            if this.profile_pick != self.profile_pick:
                this.profile_pick.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(NormalProfile, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.name + ", "+str(self.user.email)


# =========================[ User Follow-UnFollow Section ]=======================
class FollowersFollowing(models.Model):
    """
    Followers, Following By, Un Follow etc. Of an User.
    """
    followed_by = models.ManyToManyField(to=User, related_name='following', symmetrical=False)
    following_user = models.OneToOneField(to=User, unique=True, on_delete=models.CASCADE)

    # This is for Follow purpose
    @classmethod
    def follow(cls, following_user, followed_by_user):
        obj, create = cls.objects.get_or_create(following_user=following_user)
        obj.followed_by.add(followed_by_user)

    # This is for Un-Follow purpose
    @classmethod
    def un_follow(cls, following_user, followed_by_user):
        obj, create = cls.objects.get_or_create(following_user=following_user)
        obj.followed_by.remove(followed_by_user)

    @property
    def get_total_following(self):
        all_follower_users = FollowersFollowing.objects.filter(followed_by=self.following_user)
        total_following_number = all_follower_users.count()
        return total_following_number

    @property
    def get_total_followers(self):
        total_followers_number = self.followed_by.count()
        return total_followers_number

    def __str__(self):
        return "Followers Of: " + str(self.following_user) + "| Total Following:" + str(self.get_total_following) + "| Total Followers:" + str(self.get_total_followers)


# ______________________________________________________________________
#                 That Is Seller Profile Section
# ______________________________________________________________________
# class SpacialAccount(models.Model):
#     """
#     This is "SERVICE PROVIDER PROFILE" MODEL
#     Here (SerV) => (service provider)
#     """
#     Seller_name = models.CharField(max_length=50)
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
#     Seller_Store_name = models.CharField(max_length=100)
#     Seller_Store_type = models.CharField(max_length=100,
#                                               default="Grocery",
#                                               choices=(
#                                                   ("Grocery", "Grocery"),
#                                                   ("Farm", "Farm"),
#                                                   ("Medical", "Medical"),
#                                                   ("Educational Product", "Educational Product"),
#                                                   ("Electronics", "Electronics"),
#                                                   ("", "Tech"),
#                                               ))
#     Seller_particular_profession = models.CharField(max_length=255)
#     Seller_birth_date = models.DateField(null=True)
#     Seller_age = models.IntegerField(default=12, validators=[MinValueValidator(12), MaxValueValidator(80)])
#     Seller_address = models.CharField(max_length=255, default='')
#     # SerV_location_lat = models.DecimalField(max_length=12)
#     # SerV_location_lng = models.DecimalField(max_length=12)
#     Seller_phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15)
#     Seller_gender = models.CharField(max_length=10,
#                               default="Male",
#                               choices=(("Male", "Male"),
#                                        ("Female", "Female"),
#                                        ("TransGen", "TransGen")
#                                        )
#                               )
#     Seller_Profile_pick = models.ImageField(upload_to='SellerProfile/ProfileImages')
#
#     def __str__(self):
#         return '%s' % self.Seller_name
#
#     def save(self, *args, **kwargs):
#         """
#         This part is very important for uploading a file because
#         It will replace the previous file and insert the new file.
#         :return: delete old file when replacing by updating the file
#         """
#         try:
#             this = SpacialAccount.objects.get(id=self.id)
#             if this.SerV_Profile_pick != self.Seller_Profile_pick:
#                 this.SerV_Profile_pick.delete(save=False)
#         except:
#             pass  # when new photo then we do nothing, normal case
#         super(SpacialAccount, self).save(*args, **kwargs)

