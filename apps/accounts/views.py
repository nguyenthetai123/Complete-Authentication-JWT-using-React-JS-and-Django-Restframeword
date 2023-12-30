from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,permissions
from apps.accounts.serializers import UserRegisterSerializer,UserLoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.
class Registerview(APIView):
    def post(self,request,format=None):
        serializer= UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({'msg':'register success'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self,request,format=None):
        serializer= UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email= serializer.data.get('email')
        password= serializer.data.get('password')
        user = authenticate(email=email, password=password)
        return Response({'msg':'login success'},status=status.HTTP_200_OK)
