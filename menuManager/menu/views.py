# from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import MenuItem, UserModel
from .serializers import MenuItemSerializer, UserModelSerializer

from .authLogic import BasicAuthChecker
# from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated



# This one is for select all / and POST 
class MenuItemListView(ListCreateAPIView):
    #  checker Token : soigjodfigj
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    


# specific ID menu/ID
class Generic(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]



#  sign Up subs API's
class LoginUser(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


# login
# class AccountLogin():
#     pass

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     userName = serializers.CharField(required=False)
#     pswd     = serializers.CharField(required=False)

#     def validate(self, attrs):
#         username = attrs.get('username') or attrs.get('username')
#         password = attrs.get('password') or attrs.get('password')

#         try:
#             # Fetch the user from your custom UserModel
#             user = UserModel.objects.get(username=username)
#         except UserModel.DoesNotExist:
#             raise AuthenticationFailed('Invalid credentials')

#         # Check the password using Django's check_password
#         if not check_password(password, user.password):
#             raise AuthenticationFailed('Invalid credentials')

#         # Generate tokens manually
#         refresh = RefreshToken.for_user(user)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }



class AccountLogin(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
