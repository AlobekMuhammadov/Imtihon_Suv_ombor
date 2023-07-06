from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.views import APIView


class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['ism','tel']
    ordering_fields = ['qarz']



class BuyurtmaAPIView(APIView):
    def get(self,request):
        buyurtmalar = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtmalar,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        malumot = request.data
        serializer = BuyurtmaSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)







