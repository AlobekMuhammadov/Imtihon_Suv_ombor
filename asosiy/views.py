# from django.contrib.admin import filters
from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializer import *
from .models import *

class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brend']
    ordering_fields = ['narx']

class AdminAPIView(APIView):
    def get(self,request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminDetail(APIView):
    def get(self,request,pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HaydovchiAPIView(APIView):
    def get(self,request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HaydovchiDetail(APIView):
    def get(self,request,pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data, status=status.HTTP_200_OK)

