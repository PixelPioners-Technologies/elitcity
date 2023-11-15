from django_filters import rest_framework as filters
from .models import Complex

class ComplexFilter(filters.FilterSet):
    # ფილტრები მეტრ კვადრატზე
    area_from = filters.NumberFilter(field_name="space", lookup_expr='gte')
    area_to = filters.NumberFilter(field_name="space", lookup_expr='lte')

    # ფასის ფილტრი
    total_price_from = filters.NumberFilter(field_name="price_per_sq_meter", lookup_expr='gte')
    total_price_to = filters.NumberFilter(field_name="price_per_sq_meter", lookup_expr='lte')

    # დასრულებულია თუ არა
    finished = filters.BooleanFilter()

    
    class Meta:
        model = Complex
        fields = [
            'area_from', 'area_to', 
            'total_price_from', 'total_price_to', 
            'finished',
        ]
