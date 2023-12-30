from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,permissions
from apps.accounts.serializers import UserRegisterSerializer
from rest_framework.views import APIView
# Create your views here.
class Registerview(APIView):
    def post(self,request,format=None):
        serializer= UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({'msg':'register success'}, status=status.HTTP_201_CREATED)
