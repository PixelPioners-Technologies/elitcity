from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ComplexViewSet , CompanyViewSet, ApartmentViewSet,DirectAddressViewset, DistrictViewset, PharentDistrictViewset, CityViewset, ComplexImageViewSet, ApartmentImageViewSet


router = DefaultRouter()
router.register(r'complex' , ComplexViewSet , basename='complex')
router.register(r'companies' , CompanyViewSet , basename='companies' ) 
router.register(r'apartments', ApartmentViewSet)
router.register(r'directaddress', DirectAddressViewset)
router.register(r'district', DistrictViewset, basename='district')
router.register(r'pharentdistrict', PharentDistrictViewset, basename='pharentdistrict')
router.register(r'city', CityViewset, basename='city')
router.register(r'compleximage', ComplexImageViewSet, basename='compleximage')
router.register(r'apartmentimage', ApartmentImageViewSet, basename='apartmentimage')


urlpatterns = [
    path('' , include(router.urls))
]