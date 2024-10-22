from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from .filters import *
from django.db.models import F
from rest_framework.filters import OrderingFilter



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

    private_apartment_links = {
        language.language: reverse(f'{language.language.lower()}-private-apartment-list', request=request, format=format)
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

    blog_links = {
        language.language: reverse(f'{language.language.lower()}-blog-list', request=request, format=format)
        for language in Language.objects.all()
    }
    complexandappartments_links = {
        language.language: reverse(f'{language.language.lower()}-complexandappartments-list', request=request, format=format)
        for language in Language.objects.all()
    }
    companycomplex_links = {
        language.language: reverse(f'{language.language.lower()}-companycomplex-list', request=request, format=format)
        for language in Language.objects.all()
    }

    company_links['uni-data'] = reverse('uni-company-list', request=request, format=format)
    company_links['uni-images'] = reverse('uni-company-images-list', request=request, format=format)
    complex_links['uni-data'] = reverse('uni-complex-list', request=request, format=format)
    complex_links['uni-images'] = reverse('uni-complex-images-list', request=request, format=format)
    apartment_links['uni-data'] = reverse('uni-apartment-list', request=request, format=format)
    apartment_links['uni-images'] = reverse('uni-apartment-images-list', request=request, format=format)

    private_apartment_links['uni-data'] = reverse('uni-private-apartment-list' ,request=request, format=format)
    private_apartment_links['uni-images'] = reverse('uni-private-apartment-images-list' , request=request, format=format)

    ground_links['uni-data'] = reverse('uni-ground-list', request=request, format=format)
    ground_links['uni-images'] = reverse('uni-ground-images-list', request=request, format=format)

    promotions_links['uni-data'] = reverse('uni-promotions-list', request=request, format=format)
    promotions_links['uni-images'] = reverse('uni-promotions-images-list', request=request, format=format)

    blog_links['uni-data'] = reverse('uni-blog-list' ,request=request, format=format)
    blog_links['uni-images'] = reverse('uni-blog-images-list' , request=request, format=format)



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

        'pivate-Apartment': private_apartment_links, 

        'ground': ground_links,
        'promotions': promotions_links,

        'maps': map_links,
        "blogs" : blog_links,
        "complexandappartments":complexandappartments_links,
        'companycomplex': companycomplex_links,
    })

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 12
    max_limit = 100

    def get_paginated_response(self, data):
        total_items = self.queryset.count()
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_page': self.get_current_page(),
            'total_pages': self.get_total_pages(),
            'total_items': total_items,
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

    def paginate_queryset(self, queryset, request, view=None):
            self.queryset = queryset  # Store the queryset to use in get_paginated_response
            return super().paginate_queryset(queryset, request, view=view)

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

# ---------------------complex views--------------------------------------------------------
from django.db import transaction
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
import logging

logger = logging.getLogger(__name__)

class Complex_Name_Viewset(viewsets.ModelViewSet):
    queryset = Complex_Names.objects.all()
    serializer_class = Complex_Name_Serializers
    pagination_class = CustomLimitOffsetPagination



class Complex_KA_Viewset(viewsets.ModelViewSet):
    queryset = Complex_KA.objects.all()
    serializer_class = Complex_KA_Serializers
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Complex_KA_Filter
    search_fields = [
        'complex_name_ka', 
        'type_of_roof_ka',
        'internal_complex_name__internal_complex_name', 
        'internal_complex_name__full_price',  
        'internal_complex_name__price_per_sq_meter',
    ]


    def get_queryset(self):
        # Annotate the queryset with the 'price_per_sq_meter' field from the related 'Complex_Names' model.
        return self.queryset.annotate(
            price_per_sq_meter=F('internal_complex_name__price_per_sq_meter'),
            created_at=F('internal_complex_name__created_at'),
            rank=F('internal_complex_name__rank')

        )

    ordering_fields = ['price_per_sq_meter', 'created_at','rank']


class Complex_EN_Viewset(viewsets.ModelViewSet):
    queryset = Complex_EN.objects.all()
    serializer_class = Complex_EN_Serializers
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Complex_EN_Filter
    search_fields = [
        'complex_name_en', 
        'type_of_roof_en',
        'internal_complex_name__internal_complex_name', 
        'internal_complex_name__full_price',  
        'internal_complex_name__price_per_sq_meter',
    ]

    nearby = models.JSONField(default=dict)

    def get_queryset(self):
        return self.queryset.annotate(
            price_per_sq_meter=F('internal_complex_name__price_per_sq_meter'),
            created_at=F('internal_complex_name__created_at'),
            rank=F('internal_complex_name__rank')
        )

    ordering_fields = ['price_per_sq_meter', 'created_at','rank']




class Complex_RU_Viewset(viewsets.ModelViewSet):
    queryset = Complex_RU.objects.all()
    serializer_class = Complex_RU_Serializers
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Complex_RU_Filter
    search_fields = [
        'complex_name_ru', 
        'type_of_roof_ru',
        'internal_complex_name__internal_complex_name', 
        'internal_complex_name__full_price',  
        'internal_complex_name__price_per_sq_meter',
    ]

    def get_queryset(self):
        return self.queryset.annotate(
        price_per_sq_meter=F('internal_complex_name__price_per_sq_meter'),
        created_at=F('internal_complex_name__created_at'),
        rank=F('internal_complex_name__rank')


    )

    ordering_fields = ['price_per_sq_meter', 'created_at','rank']




class Complex_Images_Viewset(viewsets.ModelViewSet):
    queryset = Complex_Images.objects.all()
    serializer_class = Complex_Image_Serializers
    pagination_class = CustomLimitOffsetPagination

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
    filter_backends = [DjangoFilterBackend , OrderingFilter, SearchFilter]
    filterset_class = Apartment_KA_Filter
    search_fields = ['appartment_name_ka', 'test_field_ka']

    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_apartment_name__created_at'),
        square_price=F('internal_apartment_name__square_price'),
        full_price=F('internal_apartment_name__full_price')

    )

    ordering_fields = ['created_at', 'square_price','full_price']




class Apartment_EN_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_EN.objects.all()
    serializer_class = Appartment_EN_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    filterset_class = Apartment_EN_Filter
    search_fields = ['appartment_name_en', 'test_field_en']

    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_apartment_name__created_at'),
        square_price=F('internal_apartment_name__square_price'),
        full_price=F('internal_apartment_name__full_price')

    )

    ordering_fields = ['created_at', 'square_price','full_price']




class Apartment_RU_Viewset(viewsets.ModelViewSet):
    queryset = Appartment_RU.objects.all()
    serializer_class = Appartment_RU_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend , OrderingFilter, SearchFilter]
    filterset_class = Apartment_RU_Filter
    search_fields = ['appartment_name_ru', 'test_field_ru']

    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_apartment_name__created_at'),
        square_price=F('internal_apartment_name__square_price'),
        full_price=F('internal_apartment_name__full_price')

    )

    ordering_fields = ['created_at', 'square_price','full_price']




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


class Private_Appartment_Names_Viewset(viewsets.ModelViewSet):
    queryset = Private_Appartment_Names.objects.all()
    serializer_class = Private_Appartment_Name_Serializer
    pagination_class = CustomLimitOffsetPagination



class Private_Apartment_Images_Viewset(viewsets.ModelViewSet):
    queryset = Private_Appartment_images.objects.all()
    serializer_class = Private_Appartment_Images_Serializer
    pagination_class = CustomLimitOffsetPagination


class Private_Apartment_EN_Viewset(viewsets.ModelViewSet):
    queryset = Private_Appartment_EN.objects.all()
    serializer_class = Private_Appartment_EN_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Private_Appartment_EN_Filter
    search_fields = [   
                    'private_apartment_name_en',
                    'internal_private_apartment_name__internal_private_apartment_name',
                    'private_apartment_address_en__city_en__city_en',
                    'private_apartment_address_en__pharentDistrict_en__pharentDistrict_en',
                    'private_apartment_address_en__district_en__district_en'
                    ]
    
    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_private_apartment_name__created_at'),
        square_price=F('internal_private_apartment_name__square_price'),
        full_price=F('internal_private_apartment_name__full_price')
    )

    ordering_fields = ['created_at', 'square_price','full_price']



class Private_Apartment_KA_Viewset(viewsets.ModelViewSet):
    queryset = Private_Appartment_KA.objects.all()
    serializer_class = Private_Appartment_KA_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Private_Appartment_KA_Filter
    search_fields = [   
                    'private_apartment_name_ka',
                    'internal_private_apartment_name__internal_private_apartment_name',
                    'private_apartment_address_ka__city_ka__city_ka',
                    'private_apartment_address_ka__pharentDistrict_ka__pharentDistrict_ka',
                    'private_apartment_address_ka__district_ka__district_ka'
                    ]

    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_private_apartment_name__created_at'),
        square_price=F('internal_private_apartment_name__square_price'),
        full_price=F('internal_private_apartment_name__full_price')
    )

    ordering_fields = ['created_at', 'square_price','full_price']


class Private_Apartment_RU_Viewset(viewsets.ModelViewSet):
    queryset = Private_Appartment_RU.objects.all()
    serializer_class = Private_Appartment_RU_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    filterset_class = Private_Appartment_RU_Filter
    search_fields = [   
                    'private_apartment_name_ru',
                    'internal_private_apartment_name__internal_private_apartment_name',
                    'private_apartment_address_ru__city_ru__city_ru',
                    'private_apartment_address_ru__pharentDistrict_ru__pharentDistrict_ru',
                    'private_apartment_address_ru__district_ru__district_ru'
                    ]

    
    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_private_apartment_name__created_at'),
        square_price=F('internal_private_apartment_name__square_price'),
        full_price=F('internal_private_apartment_name__full_price')
    )

    ordering_fields = ['created_at', 'square_price','full_price']



# -------------------------------------------ground viewsets  ----------------------------------------------


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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Ground_KA_Filters
    
    search_fields = [
        'ground_name_ka', 
        'ground_address_ka__address_ka',
    ]


    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_ground_name__created_at'),
        square_price=F('internal_ground_name__square_price'),
        full_price=F('internal_ground_name__full_price'),
        rank = F('internal_ground_name__rank'),
    )

    ordering_fields = ['created_at', 'square_price','full_price', 'rank']


class Ground_EN_Viewset(viewsets.ModelViewSet):
    queryset = Ground_EN.objects.all()
    serializer_class = Ground_EN_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_class = Ground_EN_Filters
    
    
    search_fields = [
        'ground_name_en', 
        'ground_address_en__address_en',
    ]

    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_ground_name__created_at'),
        square_price=F('internal_ground_name__square_price'),
        full_price=F('internal_ground_name__full_price'),
        rank = F('internal_ground_name__rank'),
    )

    ordering_fields = ['created_at', 'square_price','full_price', 'rank']



class Ground_RU_Viewset(viewsets.ModelViewSet):
    queryset = Ground_RU.objects.all()
    serializer_class = Ground_RU_Serializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = Ground_RU_Filters
    
    search_fields = [
        'ground_name_ru', 
        'ground_address_ru__address_ru',
    ]

    def get_queryset(self):
        return self.queryset.annotate(
        created_at=F('internal_ground_name__created_at'),
        square_price=F('internal_ground_name__square_price'),
        full_price=F('internal_ground_name__full_price'),
        rank = F('internal_ground_name__rank'),
    )

    ordering_fields = ['created_at', 'square_price','full_price', 'rank']


# -------------------------------------------blog viewsets ----------------------------------------------
class Blog_Names_Viewset(viewsets.ModelViewSet):
    queryset = Blog_Names.objects.all()
    serializer_class = Blog_Names_Serializer
    pagination_class = None

class Blog_Images_Viewset(viewsets.ModelViewSet):
    queryset = Blog_Images.objects.all()
    serializer_class = Blog_Images_Serializer
    pagination_class = None

class Blog_KA_Viewset(viewsets.ModelViewSet):
    queryset = Blog_KA.objects.all()
    serializer_class = Blog_KA_Serializer
    pagination_class = None

class Blog_EN_Viewset(viewsets.ModelViewSet):
    queryset = Blog_EN.objects.all()
    serializer_class = Blog_EN_Serializer
    pagination_class = None

class Blog_RU_Viewset(viewsets.ModelViewSet):
    queryset = Blog_RU.objects.all()
    serializer_class = Blog_RU_Serializer
    pagination_class = None


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

class PromotionsAndOffers_KA_ViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_KA.objects.all()
    serializer_class = PromotionsAndOffersKASerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_class = PromotionFilters_KA
    pagination_class = None
    search_fields = [
        'promotion_name_ka', 
        'about_ka',
        'internal_promotion_name__internal_promotion_name',
        'internal_promotion_name__company__company_name',
    ]

class PromotionsAndOffers_EN_ViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_EN.objects.all()
    serializer_class = PromotionsAndOffersENSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_class = PromotionFilters_EN
    pagination_class = None
    search_fields = [
        'promotion_name_en', 
        'about_en',
        'internal_promotion_name__internal_promotion_name',
        'internal_promotion_name__company__company_name',
    ]

class PromotionsAndOffers_RU_ViewSet(viewsets.ModelViewSet):
    queryset = Promotions_and_offers_RU.objects.all()
    serializer_class = PromotionsAndOffersRUSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_class = PromotionFilters_RU
    pagination_class = None
    search_fields = [
        'promotion_name_ru', 
        'about_ru',
        'internal_promotion_name__internal_promotion_name',
        'internal_promotion_name__company__company_name',
    ]

class Complex_With_Appartment_KA_ViewSet(viewsets.ModelViewSet):
    queryset = Complex_KA.objects.all()
    serializer_class = Complex_with_appartments_KA_Serializer

class Complex_With_Appartment_EN_ViewSet(viewsets.ModelViewSet):
    queryset = Complex_EN.objects.all()
    serializer_class = Complex_with_appartments_EN_Serializer

class Complex_With_Appartment_RU_ViewSet(viewsets.ModelViewSet):
    queryset = Complex_RU.objects.all()
    serializer_class = Complex_with_appartments_RU_Serializer



class Company_Complex_KA_ViewSet(viewsets.ModelViewSet):
    queryset = Company_KA.objects.all()
    serializer_class = CompanyKASerializer

class Company_Complex_EN_ViewSet(viewsets.ModelViewSet):
    queryset = Company_EN.objects.all()
    serializer_class = CompanyENSerializer

class Company_Complex_RU_ViewSet(viewsets.ModelViewSet):
    queryset = Company_RU.objects.all()
    serializer_class = CompanyRUSerializer





from django.http import JsonResponse
import requests
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["POST"])
def google_apps_script_proxy(request):
    script_url = 'https://script.google.com/macros/s/AKfycbzgaJ6q1C4eA-fwWAwzkRv81U0FdEsQ-cnCeZa47TqfmQcEQy6NbRKU8K1TDJ49ySwA/exec'

    # Ensure the request body is correctly formatted as JSON
    data = json.loads(request.body.decode('utf-8'))
    
    try:
        # Forward the request to the Google Apps Script, ensuring JSON data is sent
        response = requests.post(script_url, json=data, headers={'Content-Type': 'application/json'})
        
        # Create a Django response object with the JSON data from Google Apps Script
        django_response = JsonResponse(response.json(), safe=False, status=response.status_code)
        
        # Set CORS headers on the Django response object
        django_response["Access-Control-Allow-Origin"] = "*"
        django_response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        django_response["Access-Control-Allow-Headers"] = "Content-Type"
        
        # Return the response from Google Apps Script to the client, with CORS headers
        return django_response
    except Exception as e:
        print("Error:", str(e))  # Log any errors
        return JsonResponse({'error': 'Failed to send data to Google Apps Script', 'details': str(e)}, status=500)
