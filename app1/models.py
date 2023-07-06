from django.contrib.auth.models import User
from django.db import models
from asosiy.models import *
from rest_framework.exceptions import APIException, ValidationError


class Mijoz(models.Model):
    ism = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=50)
    qarz = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Buyurtma(models.Model):
    suv = models.ManyToManyField(Suv)
    sana = models.DateField()
    mijoz = models.ManyToManyField(Mijoz)
    miqdor = models.IntegerField()
    umumiy_narx = models.PositiveIntegerField()
    admin = models.ManyToManyField(Admin)
    haydovchi = models.ManyToManyField(Haydovchi)

    def validate_qarz(self,qiymat):
        if qiymat > 500000:
            raise ValidationError("qarzing juda kop")
        return qiymat






