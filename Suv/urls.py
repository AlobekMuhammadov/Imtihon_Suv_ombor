from django.contrib import admin
from django.urls import path
from asosiy.views import *
from app1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("suv",SuvModelViewSet)
router.register("mijoz",SuvModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyurtmalar/', BuyurtmaAPIView.as_view()),
    path('boshqaruvchilar/', AdminAPIView.as_view()),
    path('boshqaruvchi/<int:pk/>', AdminAPIView.as_view()),
    path('haydovchilar/', HaydovchiAPIView.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiAPIView.as_view()),
    path('', include(router.urls)),
]
