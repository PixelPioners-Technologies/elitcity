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
