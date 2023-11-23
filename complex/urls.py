from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ComplexViewSet , ComplexImageViewSet, CompanyViewSet, ApartmentViewSet,DirectAddressViewset,GeoUbaniViewset,DistrictViewset,GeoCitiesViewset


router = DefaultRouter()
router.register(r'complex' , ComplexViewSet , basename='complex')
router.register(r'companies' , CompanyViewSet , basename='companies' ) 
router.register(r'images' ,  ComplexImageViewSet , basename='images' ) 
router.register(r'apartments', ApartmentViewSet)
router.register(r'geocutues', GeoCitiesViewset)
router.register(r'geoubani', GeoUbaniViewset)
router.register(r'district', DistrictViewset)
router.register(r'directaddress', DirectAddressViewset)


urlpatterns = [
    path('' , include(router.urls))
]