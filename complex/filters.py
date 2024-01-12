# --------------------------------------filtering for new structure ---------------------------------------------------

from django_filters import rest_framework as filters
from django.db.models import Q
from .models import *


class Complex_KA_Filter(filters.FilterSet):
    min_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='gte')
    max_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='lte')

    max_full_price = filters.NumberFilter(field_name='internal_complex_name__full_price' , lookup_expr='lte' )
    min_full_price = filters.NumberFilter(field_name='internal_complex_name__full_price' , lookup_expr='gte' )

    min_space = filters.NumberFilter(field_name='internal_complex_name__space', lookup_expr='gte') 
    max_space = filters.NumberFilter(field_name='internal_complex_name__space', lookup_expr='lte') 

    status = filters.MultipleChoiceFilter(field_name='internal_complex_name__status', choices=ComplexStatus.choices)

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

        min_full_price = self.request.GET.get('min_full_price')
        max_full_price = self.request.GET.get('max_full_price')


        # Apply price filters using AND logic
        if min_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__gte = min_price)
        if max_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__lte = max_price)
        if min_full_price:
            qs = qs.filter(internal_complex_name__full_price__gte = min_full_price)
        if max_full_price:
            qs = qs.filter(internal_complex_name__full_price__lte = max_full_price)

        return qs.distinct()  


class Complex_EN_Filter(filters.FilterSet):
    min_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='gte')
    max_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='lte')

    max_full_price = filters.NumberFilter(field_name='internal_complex_name__full_price' , lookup_expr='lte' )
    min_full_price = filters.NumberFilter(field_name='internal_complex_name__full_price' , lookup_expr='gte' )

    min_space = filters.NumberFilter(field_name='internal_complex_name__space', lookup_expr='gte') 
    max_space = filters.NumberFilter(field_name='internal_complex_name__space', lookup_expr='lte') 

    status = filters.MultipleChoiceFilter(field_name='internal_complex_name__status', choices=ComplexStatus.choices)

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


        min_full_price = self.request.GET.get('min_full_price')
        max_full_price = self.request.GET.get('max_full_price')


        # Apply price filters using AND logic
        if min_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__gte=min_price)
        if max_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__lte=max_price)
        if min_full_price:
            qs = qs.filter(internal_complex_name__full_price__gte = min_full_price)
        if max_full_price:
            qs = qs.filter(internal_complex_name__full_price__lte = max_full_price)

        return qs.distinct()  


class Complex_RU_Filter(filters.FilterSet):
    min_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='gte')
    max_price_per_sq_meter = filters.NumberFilter(field_name='internal_complex_name__price_per_sq_meter', lookup_expr='lte')

    max_full_price = filters.NumberFilter(field_name='internal_complex_name__full_price' , lookup_expr='lte' )
    min_full_price = filters.NumberFilter(field_name='internal_complex_name__full_price' , lookup_expr='gte' )

    min_space = filters.NumberFilter(field_name='internal_complex_name__space', lookup_expr='gte') 
    max_space = filters.NumberFilter(field_name='internal_complex_name__space', lookup_expr='lte') 

    status = filters.MultipleChoiceFilter(field_name='internal_complex_name__status', choices=ComplexStatus.choices)


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


        min_full_price = self.request.GET.get('min_full_price')
        max_full_price = self.request.GET.get('max_full_price')


        # Apply price filters using AND logic
        if min_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__gte=min_price)
        if max_price:
            qs = qs.filter(internal_complex_name__price_per_sq_meter__lte=max_price)
        if min_full_price:
            qs = qs.filter(internal_complex_name__full_price__gte = min_full_price)
        if max_full_price:
            qs = qs.filter(internal_complex_name__full_price__lte = max_full_price)


        return qs.distinct()  

