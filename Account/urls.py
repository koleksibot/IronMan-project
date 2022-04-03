from django.urls import path
from .views import (
    signup_view,
    validate_email,
    resend_account_validate_otp,
    CustomAuthToken,
    reset_password_email,
    forgot_password_change,
    who_am_i,
    auth_user_password_Change_email,
    delete_account
)


urlpatterns = [
    path('user_signup/', signup_view, name="Signup"),
    path('user_email_validate/<int:pk>/', validate_email, name="userEmailValidate"),
    path('user_New_Otp/<int:pk>/', resend_account_validate_otp, name="userNewOtp"),

    path('login/', CustomAuthToken.as_view()),

    path('forgotPassword_email/', reset_password_email, name="ResetPasswordEmail"),
    path('authenticated_UserPassword_email/<int:pk>/', auth_user_password_Change_email,
         name="Authenticated_User_Password_Change_Email"),
    path('forgot_Password_Change/<int:pk>/', forgot_password_change, name="ForgotPasswordChange"),
    path('delete_account/<int:pk>/', delete_account, name="DeleteYourAccount"),

    path('whoAmI/', who_am_i, name="whoAmI"),
]

