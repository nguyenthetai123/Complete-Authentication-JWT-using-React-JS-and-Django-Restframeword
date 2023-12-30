from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,permissions
from apps.accounts.serializers import UserRegisterSerializer,UserLoginSerializer,UserProfileSerializer,UserChangerPassword
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.tokens import RefreshToken
# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class Registerview(APIView):
    def post(self,request,format=None):
        serializer= UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token= get_tokens_for_user(user)
        return Response({'token':token,'msg':'register success'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self,request,format=None):
        serializer= UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email= serializer.data.get('email')
        password= serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not  None:
            token= get_tokens_for_user(user)
            return Response({'token':token,'msg':'login success'},status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}},
                            status=status.HTTP_404_NOT_FOUND)

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChangePasswordUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer= UserChangerPassword(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)

