# Use Only in Rest-Framework
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, UserOTPSerializers, ResetPasswordEmailSerializer, UserPasswordChangeSerializer
from Account.models import User, UserOTP
import random
import re
from .utils import Util

# For Authentication Purpose
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup_view(request):
    try:
        """
        Signup An User
        """
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            newData = {}
            if serializer.is_valid():
                account = serializer.save()

                """
                Create User First OTP
                """
                user_otp = random.randint(100000, 999999)
                user = User.object.get(id=account.id)
                # print(user.username)
                UserOTP.objects.create(user=user, otp=user_otp)

                # """
                # Sending Email To User
                # """
                # email_body = 'Hi '+account.full_name+' Thanks for register,' \
                #                                      ' verify your Email by Using Your OTP-'+str(user_otp)
                # data = {'email_body': email_body, 'to_email': account.email, 'email_subject': 'Verify Your Email'}
                # Util.send_email(data)

                """
                To finding an user it is to essential
                """
                newData['userId'] = account.id

            else:
                newData = serializer.errors
            return Response(newData)

        return Response({'true'})
    except:
        return Response({'Something Went Wrong!'})


@api_view(['POST'])
def validate_email(request, pk):
    """ ~~~~~~~~:*****:~~~~~~~~[ Validate user email ]~~~~~~~~:*****:~~~~~~~~ """
    if request.method == 'POST':
        user = User.object.get(id=pk)
        user_otp = UserOTP.objects.filter(user=user).last()
        serializer = UserOTPSerializers(data=request.data)
        serializer.is_valid()
        sender_otp = serializer.data['otp']

        """
        Checking If the Otp Is right Or wrong
        """
        if user_otp.otp == sender_otp:
            user.is_active = True
            user.save()
            new_otp = random.randint(100000, 999999)
            new_otp_add = {'otp': new_otp}
            serializer = UserOTPSerializers(instance=user_otp, data=new_otp_add)
            if serializer.is_valid():
                serializer.save()
            return Response({'true'})
        else:
            return Response({'false'})


@api_view(['POST'])
def resend_account_validate_otp(request, pk):
    """ ~~~~~~~~:*****:~~~~~~~~[ Resend email to an user for new otp ]~~~~~~~~:*****:~~~~~~~~ """
    if request.method == 'POST':
        user = User.object.get(id=pk)
        new_otp = random.randint(100000, 999999)
        new_otp_add = {'otp': new_otp}
        user_new_otp = UserOTP.objects.filter(user=user).last()
        serializer = UserOTPSerializers(instance=user_new_otp, data=new_otp_add)
        if serializer.is_valid():
            serializer.save()
        # """
        # Sending Email To User New OTP
        # """
        # email_body = 'Hi '+user.full_name+' Your New OTP-is '+str(new_otp)
        # data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify Your Email'}
        # Util.send_email(data)
        return Response({'true'})


class CustomAuthToken(ObtainAuthToken):
    """ ~~~~~~~~:*****:~~~~~~~~[ Generate Token For an User ]~~~~~~~~:*****:~~~~~~~~ """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })


@api_view(['POST'])
def reset_password_email(request):
    """ ~~~~~~~~:*****:~~~~~~~~[ Send Reset Password Email To The User ]~~~~~~~~:*****:~~~~~~~~ """
    try:
        serializer = ResetPasswordEmailSerializer(data=request.data)
        new_data = {}
        if serializer.is_valid(raise_exception=True):

            user = User.objects.get(username=serializer.data['username'], email=serializer.data['email'])
            if user is not None:
                """ Set New Otp After Validating User """
                otp_obj = UserOTP.objects.get(user=user)
                new_otp = random.randint(100000, 999999)
                otp_obj.otp = new_otp
                otp_obj.save()
                new_data['id'] = user.id

                """
                Sending New OTP Email To The User For Change Password
                """
                email_body = 'Hi '+user.full_name+' Your Password Reset OTP-is '+str(new_otp)
                data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify Your Email'}
                Util.send_email(data)
                return Response(new_data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def forgot_password_change(request, pk):
    """ ~~~~~~~~:*****:~~~~~~~~[ Resetting Password ]~~~~~~~~:*****:~~~~~~~~ """
    try:
        user = User.objects.get(id=pk)
        otp_obj = UserOTP.objects.get(user=user)
        previous_otp = otp_obj.otp
        serializer = UserPasswordChangeSerializer(data=request.data)
        print(user)

        if serializer.is_valid():
            """ Validating User """
            if (previous_otp == serializer.data['otp']) & (serializer.data['password'] == serializer.data['password2']):
                print('success')
            if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,60}$", serializer.data['password']):

                """ Set New Password After Validating User """
                user.set_password(serializer.data['password'])
                user.save()

                """ Set New Otp After Validating User """
                new_otp = random.randint(100000, 999999)
                otp_obj.otp = new_otp
                otp_obj.save()

                return Response({'success': 'success'})
            # else:
            return Response({'error': 'Otp or password do not match with password2'})
        else:
            return Response({'error': 'Otp or password do not match with password2'})
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def auth_user_password_Change_email(request, pk):
    try:
        user = User.objects.get(id=pk)
        otp_obj = UserOTP.objects.get(user=user)

        """ Set New Otp After Validating User """
        new_otp = random.randint(100000, 999999)
        otp_obj.otp = new_otp
        otp_obj.save()

        # """
        # Sending New OTP Email To The User For Change Password
        # """
        # email_body = 'Hi '+user.full_name+' Your Password Reset OTP-is '+str(new_otp)
        # data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify Your Email'}
        # Util.send_email(data)
        return Response({
            'data': 'You request for Change Password'
        })
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    return Response({'data': 'successfully delete your account'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def who_am_i(request):
    content = {'message': 'Hello, Sudipta'}
    return Response(content)

