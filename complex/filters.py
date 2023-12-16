# import django_filters
# from django.db.models import F, ExpressionWrapper, DecimalField
# from .models import Complex, Apartment

# class ComplexFilter(django_filters.FilterSet):
#     min_area = django_filters.NumberFilter(field_name='space', lookup_expr='gte')
#     max_area = django_filters.NumberFilter(field_name='space', lookup_expr='lte')
#     min_price_per_sq_meter = django_filters.NumberFilter(field_name='price_per_sq_meter', lookup_expr='gte')
#     max_price_per_sq_meter = django_filters.NumberFilter(field_name='price_per_sq_meter', lookup_expr='lte')
#     finished = django_filters.BooleanFilter(field_name='finished')

#     class Meta:
#         model = Complex
#         fields = ['min_area', 'max_area', 'min_price_per_sq_meter', 'max_price_per_sq_meter', 'finished']

# class ApartmentFilter(django_filters.FilterSet):
#     min_area = django_filters.NumberFilter(field_name='area', lookup_expr='gte')
#     max_area = django_filters.NumberFilter(field_name='area', lookup_expr='lte')
#     min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
#     max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
#     is_available = django_filters.BooleanFilter(field_name='is_available')

#     ROOM_CHOICES = [
#         ('studio', 'Studio'),
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5+', '5+'),
#     ]

#     number_of_rooms = django_filters.MultipleChoiceFilter(choices=ROOM_CHOICES, method='filter_number_of_rooms')

#     def filter_number_of_rooms(self, queryset, name, values):
#         if '5+' in values:
#             queryset = queryset.filter(number_of_rooms__gte=5)
#         else:
#             queryset = queryset.filter(number_of_rooms__in=[int(v) if v.isdigit() else v for v in values])
#         return queryset
    

#     min_price_per_sqm = django_filters.NumberFilter(method='filter_min_price_per_sqm')
#     max_price_per_sqm = django_filters.NumberFilter(method='filter_max_price_per_sqm')

#     def filter_min_price_per_sqm(self, queryset, name, value):
#         queryset = queryset.annotate(
#             price_per_sqm=ExpressionWrapper(
#                 F('price') / F('area'), 
#                 output_field=DecimalField(max_digits=12, decimal_places=2)
#             )
#         )
#         return queryset.filter(price_per_sqm__gte=value)

#     def filter_max_price_per_sqm(self, queryset, name, value):
#         queryset = queryset.annotate(
#             price_per_sqm=ExpressionWrapper(
#                 F('price') / F('area'), 
#                 output_field=DecimalField(max_digits=12, decimal_places=2)
#             )
#         )
#         return queryset.filter(price_per_sqm__lte=value)

#     class Meta:
#         model = Apartment
#         fields = ['min_area', 'max_area', 'min_price', 'max_price', 'number_of_rooms', 'is_available','min_price_per_sqm', 'max_price_per_sqm']


# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------filtering for new structure ---------------------------------------------------

from django_filters import rest_framework as filters
from django.db.models import Q
from .models import *


class Complex_KA_Filter(filters.FilterSet):
    min_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='gte')
    max_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='lte')

    class Meta:
        model = Complex_KA
        fields = {
            'address_ka__city_ka__city_ka': ['exact', 'icontains'],
        }


    @property
    def qs(self):
        parent_name_in = self.request.GET.get('address_ka__pharentDistrict_ka__pharentDistrict_ka__in')
        district_name_in = self.request.GET.get('address_ka__district_ka__district_ka__in')

        parent_districts = parent_name_in.split(',') if parent_name_in else []
        districts = district_name_in.split(',') if district_name_in else []

        if not self.is_bound:
            return self.queryset

        # Base queryset using the existing filters
        base_qs = super(Complex_KA_Filter, self).qs

        # Create Q objects for additional OR logic
        parent_district_q = Q(address_ka__pharentDistrict_ka__pharentDistrict_ka__in=parent_districts) if parent_districts else Q()
        district_q = Q(address_ka__district_ka__district_ka__in=districts) if districts else Q()

        # Apply combined Q objects using OR
        qs = base_qs.filter(parent_district_q | district_q)

        min_price = self.request.GET.get('min_price_per_sq_meter')
        max_price = self.request.GET.get('max_price_per_sq_meter')

        # Apply price filters using AND logic
        if min_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__gte=min_price)
        if max_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__lte=max_price)

        return qs.distinct()  


class Complex_EN_Filter(filters.FilterSet):
    min_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='gte')
    max_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='lte')

    class Meta:
        model = Complex_EN
        fields = {
            'address_en__city_en__city_en': ['exact', 'icontains'],
        }

    @property
    def qs(self):
        parent_name_in = self.request.GET.get('address_en__pharentDistrict_en__pharentDistrict_en__in')
        district_name_in = self.request.GET.get('address_en__district_en__district_en__in')

        parent_districts = parent_name_in.split(',') if parent_name_in else []
        districts = district_name_in.split(',') if district_name_in else []

        if not self.is_bound:
            return self.queryset

        # Base queryset using the existing filters
        base_qs = super(Complex_EN_Filter, self).qs

        # Create Q objects for additional OR logic
        parent_district_q = Q(address_en__pharentDistrict_en__pharentDistrict_en__in=parent_districts) if parent_districts else Q()
        district_q = Q(address_en__district_en__district_en__in=districts) if districts else Q()

        # Apply combined Q objects using OR
        qs = base_qs.filter(parent_district_q | district_q)

        min_price = self.request.GET.get('min_price_per_sq_meter')
        max_price = self.request.GET.get('max_price_per_sq_meter')

        # Apply price filters using AND logic
        if min_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__gte=min_price)
        if max_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__lte=max_price)

        return qs.distinct()  


class Complex_RU_Filter(filters.FilterSet):
    min_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='gte')
    max_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='lte')


    class Meta:
        model = Complex_RU
        fields = {
            'address_ru__city_ru__city_ru': ['exact', 'icontains'],
        }

    @property
    def qs(self):
        parent_name_in = self.request.GET.get('address_ru__pharentDistrict_ru__pharentDistrict_ru__in')
        district_name_in = self.request.GET.get('address_ru__district_ru__district_ru__in')

        parent_districts = parent_name_in.split(',') if parent_name_in else []
        districts = district_name_in.split(',') if district_name_in else []

        if not self.is_bound:
            return self.queryset

        # Base queryset using the existing filters
        base_qs = super(Complex_RU_Filter, self).qs

        # Create Q objects for additional OR logic
        parent_district_q = Q(address_ru__pharentDistrict_ru__pharentDistrict_ru__in=parent_districts) if parent_districts else Q()
        district_q = Q(address_ru__district_ru__district_ru__in=districts) if districts else Q()

        # Apply combined Q objects using OR
        qs = base_qs.filter(parent_district_q | district_q)

        min_price = self.request.GET.get('min_price_per_sq_meter')
        max_price = self.request.GET.get('max_price_per_sq_meter')

        # Apply price filters using AND logic
        if min_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__gte=min_price)
        if max_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__lte=max_price)

        return qs.distinct()  

