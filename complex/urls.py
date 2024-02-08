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
ground_routers = DefaultRouter()
blog_routers = DefaultRouter()
promotions_routers = DefaultRouter()
complex_apartments = DefaultRouter()
# company_complex = DefaultRouter()


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

ground_routers.register(r'uni', Ground_Names_Viewset, basename='uni-ground')
ground_routers.register(r'images', Ground_Images_Viewset, basename='uni-ground-images')
ground_routers.register(r'ka', Ground_KA_Viewset, basename='ka-ground')
ground_routers.register(r'en', Ground_EN_Viewset, basename='en-ground')
ground_routers.register(r'ru', Ground_RU_Viewset, basename='ru-ground')


blog_routers.register(r'uni', Blog_Names_Viewset, basename='uni-blog')
blog_routers.register(r'images', Blog_Images_Viewset, basename='uni-blog-images')
blog_routers.register(r'ka', Blog_KA_Viewset, basename='ka-blog')
blog_routers.register(r'en', Blog_EN_Viewset, basename='en-blog')
blog_routers.register(r'ru', Blog_RU_Viewset, basename='ru-blog')


promotions_routers.register(r'uni', PromotionsAndOffersNamesViewSet, basename='uni-promotions')
promotions_routers.register(r'images', PromotionsAndOffersImageViewSet, basename='uni-promotions-images')
promotions_routers.register(r'ka', PromotionsAndOffers_KA_ViewSet, basename='ka-promotions')
promotions_routers.register(r'en', PromotionsAndOffers_EN_ViewSet, basename='en-promotions')
promotions_routers.register(r'ru', PromotionsAndOffers_RU_ViewSet, basename='ru-promotions')


complex_apartments.register(r'ka', Complex_With_Appartment_KA_ViewSet, basename='ka-complexandappartments' )
complex_apartments.register(r'en', Complex_With_Appartment_EN_ViewSet, basename='en-complexandappartments' )
complex_apartments.register(r'ru', Complex_With_Appartment_RU_ViewSet, basename='ru-complexandappartments' )

# company_complex.register(r'ka', Company_Complex_KA_ViewSet, basename='ka-companycomplex' )
# company_complex.register(r'en', Company_Complex_EN_ViewSet, basename='en-companycomplex' )
# company_complex.register(r'ru', Company_Complex_RU_ViewSet, basename='ru-companycomplex' )


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
    path('ground/' , include(ground_routers.urls)),
    path('map/',include(map_routers.urls)),
    path('blog/', include(blog_routers.urls)),
    path('promotions/', include(promotions_routers.urls)),
    path('complexandappartments/', include(complex_apartments.urls)),
    # path('companycomplex/',include(company_complex.urls))
]
