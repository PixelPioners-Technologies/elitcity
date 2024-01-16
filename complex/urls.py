from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
city_ruters = DefaultRouter()
pharentDistrict_routers = DefaultRouter()
district_routers = DefaultRouter()
street_name_routers = DefaultRouter()
address_routers = DefaultRouter()
company_routers = DefaultRouter()
complex_routers = DefaultRouter()
apartment_routers = DefaultRouter()
private_apartment_routers = DefaultRouter()
map_routers = DefaultRouter()

router.register(r'language',LanguageViewset, basename="language")
city_ruters.register(r'ka', City_KA_Viewset, basename='ka-city')
city_ruters.register(r'en', City_EN_Viewset, basename='en-city')
city_ruters.register(r'ru', City_RU_Viewset, basename='ru-city')

pharentDistrict_routers.register(r'ka', PharentDistrict_KA_Viewset, basename='ka-pharentdistrict')
pharentDistrict_routers.register(r'en', PharentDistrict_EN_Viewset, basename='en-pharentdistrict')
pharentDistrict_routers.register(r'ru', PharentDistrict_RU_Viewset, basename='ru-pharentdistrict')

district_routers.register(r'ka', District_KA_Viewset, basename='ka-district')
district_routers.register(r'en', District_EN_Viewset, basename='en-district')
district_routers.register(r'ru', District_RU_Viewset, basename='ru-district')

street_name_routers.register(r'ka', Street_Name_KA_Viewset, basename='ka-streetname')
street_name_routers.register(r'en', Street_Name_EN_Viewset, basename='en-streetname')
street_name_routers.register(r'ru', Street_Name_RU_Viewset, basename='ru-streetname')

address_routers.register(r'ka', Address_KA_Viewset, basename='ka-address')
address_routers.register(r'en', Address_EN_Viewset, basename='en-address')
address_routers.register(r'ru', Address_RU_Viewset, basename='ru-address')

company_routers.register(r'uni', Company_Name_Viewset, basename='uni-company')
company_routers.register(r'images', Company_Images_Viewset, basename='uni-company-images')
company_routers.register(r'ka', Company_KA_Viewset, basename='ka-company')
company_routers.register(r'en', Company_EN_Viewset, basename='en-company')
company_routers.register(r'ru', Company_RU_Viewset, basename='ru-company')

complex_routers.register(r'uni', Complex_Name_Viewset, basename='uni-complex')
complex_routers.register(r'images', Complex_Images_Viewset, basename='uni-complex-images')
complex_routers.register(r'ka', Complex_KA_Viewset, basename='ka-complex')
complex_routers.register(r'en', Complex_EN_Viewset, basename='en-complex')
complex_routers.register(r'ru', Complex_RU_Viewset, basename='ru-complex')

apartment_routers.register(r'uni', Apartment_Names_Viewset, basename='uni-apartment')
apartment_routers.register(r'images', Apartment_Images_Viewset, basename='uni-apartment-images')
apartment_routers.register(r'ka', Apartment_KA_Viewset, basename='ka-apartment')
apartment_routers.register(r'en', Apartment_EN_Viewset, basename='en-apartment')
apartment_routers.register(r'ru', Apartment_RU_Viewset, basename='ru-apartment')

private_apartment_routers.register(r'uni' ,Private_Appartment_Names_Viewset , basename='uni-private-apartment'   )
private_apartment_routers.register(r'images' , Private_Apartment_Images_Viewset , basename='uni-private-apartment-images')
private_apartment_routers.register(r'ka', Private_Apartment_KA_Viewset, basename='ka-private-apartment')
private_apartment_routers.register(r'en', Private_Apartment_EN_Viewset, basename='en-private-apartment')
private_apartment_routers.register(r'ru', Private_Apartment_RU_Viewset, basename='ru-private-apartment')


map_routers.register(r'ka', Map_KA_Viewset, basename='ka-map')
map_routers.register(r'en', Map_EN_Viewset, basename='en-map')
map_routers.register(r'ru', Map_RU_Viewset, basename='ru-map')


urlpatterns = [
    path('', api_root),
    path('' , include(router.urls)),
    path('city/' , include(city_ruters.urls)),
    path('pharentdistrict/' , include(pharentDistrict_routers.urls)),
    path('district/' , include(district_routers.urls)),
    path('streetname/' , include(street_name_routers.urls)),
    path('address/' , include(address_routers.urls)),
    path('company/' , include(company_routers.urls)),
    path('complex/' , include(complex_routers.urls)),
    path('apartment/' , include(apartment_routers.urls)),
    path('privateapartments/' , include(private_apartment_routers.urls)),
    path('map/',include(map_routers.urls)),
]
