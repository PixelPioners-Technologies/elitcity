from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ComplexViewSet , ComplexImageViewSet, CompanyListCreateView, CompanyDetailView


router = DefaultRouter()
router.register(r'complex' , ComplexViewSet , basename='complex')
router.register(r'images' ,  ComplexImageViewSet , basename='images' ) 


urlpatterns = [
    path('' , include(router.urls)),
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
]