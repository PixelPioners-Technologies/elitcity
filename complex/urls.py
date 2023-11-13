from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ComplexViewSet


router = DefaultRouter()
router.register(r'complex' , ComplexViewSet)


urlpatterns = [
    path('' , include(router.urls))
]