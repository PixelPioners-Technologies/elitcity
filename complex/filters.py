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

from .models import Complex_EN
import django_filters
from .models import Complex_EN , Complex_KA , Complex_RU



class Complex_KA_Filter(django_filters.FilterSet):
    class Meta:
        model = Complex_KA
        fields = {
            'address_ka__city_ka__city_ka': ['exact', 'icontains'],
            'address_ka__pharentDistrict_ka__pharentDistrict_ka': ['exact', 'icontains' , 'in'],
            'address_ka__district_ka__district_ka': ['exact', 'icontains', 'in'],
        }


class Complex_EN_Filter(django_filters.FilterSet):
    class Meta:
        model = Complex_EN
        fields = {
            'address_en__city_en__city_en': ['exact', 'icontains'],
            'address_en__pharentDistrict_en__pharentDistrict_en': ['exact', 'icontains', 'in'],
            'address_en__district_en__district_en': ['exact', 'icontains', 'in'],
        }




class Complex_RU_Filter(django_filters.FilterSet):
    class Meta:
        model = Complex_RU
        fields = {
            'address_ru__city_ru__city_ru': ['exact', 'icontains'],
            'address_ru__pharentDistrict_ru__pharentDistrict_ru': ['exact', 'icontains', 'in'],
            'address_ru__district_ru__district_ru': ['exact', 'icontains', 'in'],
        }
