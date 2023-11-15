from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ComplexViewSet , ComplexImageViewSet, CompanyViewSet


router = DefaultRouter()
router.register(r'complex' , ComplexViewSet , basename='complex')
router.register(r'companies' , CompanyViewSet , basename='companies' ) 
router.register(r'images' ,  ComplexImageViewSet , basename='images' ) 

urlpatterns = [
    path('' , include(router.urls))
]