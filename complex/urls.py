from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ComplexViewSet , ComplexImageViewSet


router = DefaultRouter()
router.register(r'complex' , ComplexViewSet , basename='complex')
router.register(r'images' ,  ComplexImageViewSet , basename='images' ) 


urlpatterns = [
    path('' , include(router.urls))
]