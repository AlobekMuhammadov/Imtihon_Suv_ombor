from .models import *
from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer


class SuvSerializer(ModelSerializer):
    class Meta:
        model = Suv.objects.all()
        fields = '__all__'

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin.objects.all()
        fields = '__all__'


class HaydovchiSerializer(ModelSerializer):
    class Meta:
        model = Haydovchi.objects.all()
        fields = '__all__'










