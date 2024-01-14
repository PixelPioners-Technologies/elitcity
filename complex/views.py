from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination

@api_view(['GET'])
def api_root(request, format=None):
    city_links = {
        language.language: reverse(f'{language.language.lower()}-city-list', request=request, format=format)
        for language in Language.objects.all()
    }

    pharent_district_links = {
        language.language: reverse(f'{language.language.lower()}-pharentdistrict-list', request=request, format=format)
        for language in Language.objects.all()
    }
    district_links = {
        language.language: reverse(f'{language.language.lower()}-district-list', request=request, format=format)
        for language in Language.objects.all()
    }
    street_links = {
        language.language: reverse(f'{language.language.lower()}-streetname-list', request=request, format=format)
        for language in Language.objects.all()
    }
    address_links = {
        language.language: reverse(f'{language.language.lower()}-address-list', request=request, format=format)
        for language in Language.objects.all()
    }
    company_links = {
        language.language: reverse(f'{language.language.lower()}-company-list', request=request, format=format)
        for language in Language.objects.all()
    }
    complex_links = {
        language.language: reverse(f'{language.language.lower()}-complex-list', request=request, format=format)
        for language in Language.objects.all()
    }
    apartment_links = {
        language.language: reverse(f'{language.language.lower()}-apartment-list', request=request, format=format)
        for language in Language.objects.all()
    }
    map_links = {
        language.language: reverse(f'{language.language.lower()}-map-list', request=request, format=format)
        for language in Language.objects.all()
    }
    ground_links = {
        language.language: reverse(f'{language.language.lower()}-ground-list', request=request, format=format)
        for language in Language.objects.all()
    }
    promotions_links = {
        language.language: reverse(f'{language.language.lower()}-promotions-list', request=request, format=format)
        for language in Language.objects.all()
    }
    company_links['uni-data'] = reverse('uni-company-list', request=request, format=format)
    company_links['uni-images'] = reverse('uni-company-images-list', request=request, format=format)
    complex_links['uni-data'] = reverse('uni-complex-list', request=request, format=format)
    complex_links['uni-images'] = reverse('uni-complex-images-list', request=request, format=format)
    apartment_links['uni-data'] = reverse('uni-apartment-list', request=request, format=format)
    apartment_links['uni-images'] = reverse('uni-apartment-images-list', request=request, format=format)
    ground_links['uni-data'] = reverse('uni-ground-list', request=request, format=format)
    ground_links['uni-images'] = reverse('uni-ground-images-list', request=request, format=format)
    promotions_links['uni-data'] = reverse('uni-promotions-list', request=request, format=format)
    promotions_links['uni-images'] = reverse('uni-promotions-images-list', request=request, format=format)

    return Response({
        'language': reverse('language-list', request=request, format=format),
        'city': city_links,
        'pharentDistrict': pharent_district_links,
        'district': district_links,
        'streetname': street_links,
        'address': address_links,
        'company':company_links,
        'complex':complex_links,
        'apartment': apartment_links,
        'ground': ground_links,
        'maps': map_links,
        'promotions': promotions_links,
    })

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page': self.get_current_page(),
            'total_pages': self.get_total_pages(),
            'results': data,
        })

    def get_current_page(self):
        if self.limit is None:
            return None
        return self.offset // self.limit + 1

    def get_total_pages(self):
        if self.limit is None:
            return None
        return (self.count + self.limit - 1) // self.limit


class City_KA_Viewset(viewsets.ModelViewSet):
    queryset = City_KA.objects.all()
    serializer_class = City_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class City_EN_Viewset(viewsets.ModelViewSet):
    queryset = City_EN.objects.all()
    serializer_class = City_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class City_RU_Viewset(viewsets.ModelViewSet):
    queryset = City_RU.objects.all()
    serializer_class = City_RU_Serializer
    pagination_class = CustomLimitOffsetPagination

class PharentDistrict_KA_Viewset(viewsets.ModelViewSet):
    queryset = PharentDistrict_KA.objects.all()
    serializer_class = PharentDistrict_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class PharentDistrict_EN_Viewset(viewsets.ModelViewSet):
    queryset = PharentDistrict_EN.objects.all()
    serializer_class = PharentDistrict_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class PharentDistrict_RU_Viewset(viewsets.ModelViewSet):
    queryset = PharentDistrict_RU.objects.all()
    serializer_class = PharentDistrict_RU_Serializer
    pagination_class = CustomLimitOffsetPagination
    
class District_KA_Viewset(viewsets.ModelViewSet):
    queryset = District_KA.objects.all()
    serializer_class = District_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class District_EN_Viewset(viewsets.ModelViewSet):
    queryset = District_EN.objects.all()
    serializer_class = District_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class District_RU_Viewset(viewsets.ModelViewSet):
    queryset = District_RU.objects.all()
    serializer_class = District_RU_Serializer
    pagination_class = CustomLimitOffsetPagination

class Street_Name_KA_Viewset(viewsets.ModelViewSet):
    queryset = Street_Name_KA.objects.all()
    serializer_class = Street_Name_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class Street_Name_EN_Viewset(viewsets.ModelViewSet):
    queryset = Street_Name_EN.objects.all()
    serializer_class = Street_Name_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class Street_Name_RU_Viewset(viewsets.ModelViewSet):
    queryset = Street_Name_RU.objects.all()
    serializer_class = Street_Name_RU_Serializer
    pagination_class = CustomLimitOffsetPagination

class Address_KA_Viewset(viewsets.ModelViewSet):
    queryset = Address_KA.objects.all()
    serializer_class = Address_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class Address_EN_Viewset(viewsets.ModelViewSet):
    queryset = Address_EN.objects.all()
    serializer_class = Address_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class Address_RU_Viewset(viewsets.ModelViewSet):
    queryset = Address_RU.objects.all()
    serializer_class = Address_RU_Serializer
    pagination_class = CustomLimitOffsetPagination

class LanguageViewset(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LangSerializer
    pagination_class = CustomLimitOffsetPagination

class Company_Name_Viewset(viewsets.ModelViewSet):
    queryset = Company_Names.objects.all()
    serializer_class = Company_name_serializers
    pagination_class = CustomLimitOffsetPagination

class Company_KA_Viewset(viewsets.ModelViewSet):
    queryset = Company_KA.objects.all()
    serializer_class = Company_KA_serializers
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name_ka', 'address_ka'] 
    
class Company_EN_Viewset(viewsets.ModelViewSet):
    queryset = Company_EN.objects.all()
    serializer_class = Company_EN_serializers
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name_en', 'address_en'] 

class Company_RU_Viewset(viewsets.ModelViewSet):
    queryset = Company_RU.objects.all()
    serializer_class = Company_RU_serializers
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name_ru', 'address_ru']

class Company_Images_Viewset(viewsets.ModelViewSet):
    queryset = Company_Images.objects.all()
    serializer_class = Company_Image_serializers
    pagination_class = CustomLimitOffsetPagination

class Complex_Name_Viewset(viewsets.ModelViewSet):
    queryset = Complex_Names.objects.all()
    serializer_class = Complex_Name_Serializers
    pagination_class = CustomLimitOffsetPagination

# -----------------------------------------------------------------------------
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import F
from .filters import Complex_KA_Filter, Complex_EN_Filter, Complex_RU_Filter

class BaseComplexViewSet(viewsets.ModelViewSet):
    # pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = self.model.objects.all()
        self.serializer_class = self.serializer_class
        self.filterset_class = self.filterset_class
        self.search_fields = self.search_fields

    def get_queryset(self):
        return self.queryset.annotate(
            price_per_sq_meter=F('internal_complex_name__price_per_sq_meter'),
            created_at=F('internal_complex_name__created_at'),
            rank=F('internal_complex_name__rank')
        )

    ordering_fields = ['price_per_sq_meter', 'created_at', 'rank']

class Complex_KA_Viewset(BaseComplexViewSet):
    model = Complex_KA
    serializer_class = Complex_KA_Serializers
    filterset_class = Complex_KA_Filter
    search_fields = ['=complex_name_ka', 'address_ka__address_ka', 'address_ka__city_ka__city_ka']

class Complex_EN_Viewset(BaseComplexViewSet):
    model = Complex_EN
    serializer_class = Complex_EN_Serializers
    filterset_class = Complex_EN_Filter
    search_fields = ['=complex_name_en', 'address_en__address_en', 'address_en__city_en__city_en']

class Complex_RU_Viewset(BaseComplexViewSet):
    model = Complex_RU
    serializer_class = Complex_RU_Serializers
    filterset_class = Complex_RU_Filter
    search_fields = ['=complex_name_ru', 'address_ru__address_ru', 'address_ru__city_ru__city_ru']





class Complex_Images_Viewset(viewsets.ModelViewSet):
    queryset = Complex_Images.objects.all()
    serializer_class = Complex_Image_Serializers
    pagination_class = CustomLimitOffsetPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = Complex_EN_Filter



class Apartment_Names_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_Names.objects.all()
    serializer_class = Appartment_Names_Serializer
    pagination_class = CustomLimitOffsetPagination

class Apartment_Images_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_Images.objects.all()
    serializer_class = Appartment_Images_Serializer
    pagination_class = CustomLimitOffsetPagination

class Apartment_KA_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_KA.objects.all()
    serializer_class = Appartment_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class Apartment_EN_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_EN.objects.all()
    serializer_class = Appartment_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class Apartment_RU_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_RU.objects.all()
    serializer_class = Appartment_RU_Serializer
    pagination_class = CustomLimitOffsetPagination

class Map_KA_Viewset(viewsets.ModelViewSet):
    queryset = City_KA.objects.all()
    serializer_class = City_KA_ForMap_Serializer
    pagination_class = None

class Map_EN_Viewset(viewsets.ModelViewSet):
    queryset = City_EN.objects.all()
    serializer_class = City_EN_ForMap_Serializer
    pagination_class = None

class Map_RU_Viewset(viewsets.ModelViewSet):
    queryset = City_RU.objects.all()
    serializer_class = City_RU_ForMap_Serializer
    pagination_class = None


class Ground_Names_Viewset(viewsets.ModelViewSet):
    queryset = Ground_Names.objects.all()
    serializer_class = Ground_Names_Serializer
    pagination_class = CustomLimitOffsetPagination

class Ground_Images_Viewset(viewsets.ModelViewSet):
    queryset = Ground_Images.objects.all()
    serializer_class = Ground_Images_Serializer
    pagination_class = CustomLimitOffsetPagination

class Ground_KA_Viewset(viewsets.ModelViewSet):
    queryset = Ground_KA.objects.all()
    serializer_class = Ground_KA_Serializer
    pagination_class = CustomLimitOffsetPagination

class Ground_EN_Viewset(viewsets.ModelViewSet):
    queryset = Ground_EN.objects.all()
    serializer_class = Ground_EN_Serializer
    pagination_class = CustomLimitOffsetPagination

class Ground_RU_Viewset(viewsets.ModelViewSet):
    queryset = Ground_RU.objects.all()
    serializer_class = Ground_RU_Serializer
    pagination_class = CustomLimitOffsetPagination


'''
----------------------------------------------------------------
            PROMOTIONS VIEW
----------------------------------------------------------------    
'''

from .models import (Promotions_and_offers_Names, Promotions_and_offers_KA, 
                     Promotions_and_offers_EN, Promotions_and_offers_RU,
                     Promotions_and_offers_Images)

from .serializers import (PromotionsAndOffersNamesSerializer,
                          PromotionsAndOffersKASerializer, 
                          PromotionsAndOffersENSerializer, 
                          PromotionsAndOffersRUSerializer,
                          PromotionsAndOffersImagesSerializer)

class PromotionsAndOffersNamesViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_Names.objects.all()
    serializer_class = PromotionsAndOffersNamesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['internal_promotion_name', 'company__name']

class PromotionsAndOffersImageViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_Images.objects.all()
    serializer_class = PromotionsAndOffersImagesSerializer

class PromotionsAndOffersKAViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_KA.objects.all()
    serializer_class = PromotionsAndOffersKASerializer
    filter_backends = [SearchFilter]
    search_fields = ['promotion_name_ka']

class PromotionsAndOffersENViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_EN.objects.all()
    serializer_class = PromotionsAndOffersENSerializer
    filter_backends = [SearchFilter]
    search_fields = ['promotion_name_en']

class PromotionsAndOffersRUViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_RU.objects.all()
    serializer_class = PromotionsAndOffersRUSerializer
    filter_backends = [SearchFilter]
    search_fields = ['promotion_name_ru']
