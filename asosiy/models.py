from django.contrib.auth.models import User
from django.db import models

class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    litr = models.IntegerField()
    batafsil = models.TextField(null=True,blank=True)



class Admin(models.Model):
    ism = models.CharField(max_length=17)
    yosh = models.SmallIntegerField()
    ish_vaqti = models.CharField(max_length=40)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Haydovchi(models.Model):
    ism = models.CharField(max_length=17)
    tel = models.CharField(max_length=20)
    kiritilgan_sana = models.DateField(auto_now=True)
    prava_raqam = models.IntegerField()






