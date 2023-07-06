from .models import *
from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer


class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz.objects.all()
        fields = '__all__'


class BuyurtmaSerializer(ModelSerializer):
    class Meta:
        model = Buyurtma.objects.all()
        fields = '__all__'












