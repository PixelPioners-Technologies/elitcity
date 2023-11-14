from django.urls import path , include
from rest_framework import routers
from .views import CityLocationViewSet


router = routers.DefaultRouter()

router.register(r'location' , CityLocationViewSet , 'location')

urlpatterns = [
    path('' , include(router.urls))
]