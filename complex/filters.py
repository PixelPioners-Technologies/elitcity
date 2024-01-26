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



# ---------------------------------------------Apartment fiklters ---------------------------------------------------------
    
class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass



class Apartment_EN_Filter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_apartment_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_apartment_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_apartment_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_apartment_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_apartment_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_apartment_name__square_price", lookup_expr='lte')

    status = filters.MultipleChoiceFilter(
        field_name = 'internal_apartment_name__status',
        choices = Appartment_Names.STATUS_CHOICES
    )
    
    number_of_rooms = filters.MultipleChoiceFilter(
        field_name='internal_apartment_name__number_of_rooms', 
        choices=Appartment_Names.NUMBER_OF_ROOM_CHOICES
    )

    city = filters.CharFilter(field_name='appartment_address_en__city_en__city_en', lookup_expr='icontains')


    parent_districts = CharInFilter(
        field_name='appartment_address_en__pharentDistrict_en__pharentDistrict_en', 
        lookup_expr='in', method='filter_parent_districts'
    )

    districts = CharInFilter(
        field_name='appartment_address_en__district_en__district_en', 
        lookup_expr='in', method='filter_districts'
    )

    def filter_parent_districts(self, queryset, name, value):
        if not value:
            return queryset
        filter_query = Q()
        for item in value:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, value):
        if not value:
            return queryset
        filter_query = Q()
        for item in value:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)
    

    class Meta:
        model = Appartment_EN
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'number_of_rooms', 'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]


class Apartment_KA_Filter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_apartment_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_apartment_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_apartment_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_apartment_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_apartment_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_apartment_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_apartment_name__status',
        choices = Appartment_Names.STATUS_CHOICES
    )
    

    number_of_rooms = filters.MultipleChoiceFilter(
        field_name='internal_apartment_name__number_of_rooms', 
        choices=Appartment_Names.NUMBER_OF_ROOM_CHOICES
    )

    city = filters.CharFilter(field_name='appartment_address_ka__city_ka__city_ka', lookup_expr='icontains')


    parent_districts = CharInFilter(
        field_name='appartment_address_ka__pharentDistrict_ka__pharentDistrict_ka', 
        lookup_expr='in', method='filter_parent_districts'
    )

    districts = CharInFilter(
        field_name='appartment_address_ka__district_ka__district_ka', 
        lookup_expr='in', method='filter_districts'
    )

    def filter_parent_districts(self, queryset, name, value):
        if not value:
            return queryset
        filter_query = Q()
        for item in value:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, value):
        if not value:
            return queryset
        filter_query = Q()
        for item in value:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)
    

    class Meta: 
        model = Appartment_KA
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'number_of_rooms', 'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]


class Apartment_RU_Filter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_apartment_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_apartment_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_apartment_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_apartment_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_apartment_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_apartment_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_apartment_name__status',
        choices = Appartment_Names.STATUS_CHOICES
    )
    

    number_of_rooms = filters.MultipleChoiceFilter(
        field_name='internal_apartment_name__number_of_rooms', 
        choices=Appartment_Names.NUMBER_OF_ROOM_CHOICES
    )

    city = filters.CharFilter(field_name='appartment_address_ru__city_ru__city_ru', lookup_expr='icontains')


    parent_districts = CharInFilter(
        field_name='appartment_address_ru__pharentDistrict_ru__pharentDistrict_ru', 
        lookup_expr='in', method='filter_parent_districts'
    )

    districts = CharInFilter(
        field_name='appartment_address_ru__district_ru__district_ru', 
        lookup_expr='in', method='filter_districts'
    )

    def filter_parent_districts(self, queryset, name, value):
        if not value:
            return queryset
        filter_query = Q()
        for item in value:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, value):
        if not value:
            return queryset
        filter_query = Q()
        for item in value:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)
    


    class Meta:
        model = Appartment_RU
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'number_of_rooms', 'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]

# 'parent_districts', 'districts'
        
# --------------------------------------------Private Appartments Fikters ---------------------------------------

class Private_Appartment_KA_Filter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_private_apartment_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_private_apartment_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_private_apartment_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_private_apartment_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_private_apartment_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_private_apartment_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_private_apartment_name__status',
        choices = Private_Appartment_Names.STATUS_CHOICES
    )
    

    number_of_rooms = filters.MultipleChoiceFilter(
        field_name='internal_private_apartment_name__number_of_rooms', 
        choices=Private_Appartment_Names.NUMBER_OF_ROOM_CHOICES
    )

    city = filters.CharFilter(field_name='private_apartment_address_ka__city_ka__city_ka', lookup_expr='icontains')

    parent_districts = CharInFilter(
        field_name='private_apartment_address_ka__pharentDistrict_ka__pharentDistrict_ka', 
        lookup_expr='in', method='filter_parent_districts'
    )
    districts = CharInFilter(
        field_name='private_apartment_address_ka__district_ka__district_ka', 
        lookup_expr='in', method='filter_districts'
    )

    def filter_parent_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)
    
    class Meta: 
        model = Private_Appartment_KA
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'number_of_rooms', 'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]





class Private_Appartment_EN_Filter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_private_apartment_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_private_apartment_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_private_apartment_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_private_apartment_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_private_apartment_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_private_apartment_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_private_apartment_name__status',
        choices = Private_Appartment_Names.STATUS_CHOICES
    )
    

    number_of_rooms = filters.MultipleChoiceFilter(
        field_name='internal_private_apartment_name__number_of_rooms', 
        choices=Private_Appartment_Names.NUMBER_OF_ROOM_CHOICES
    )

    city = filters.CharFilter(field_name='private_apartment_address_en__city_en__city_en', lookup_expr='icontains')

    parent_districts = CharInFilter(
        field_name='private_apartment_address_en__pharentDistrict_en__pharentDistrict_en', 
        lookup_expr='in', method='filter_parent_districts'
    )
    districts = CharInFilter(
        field_name='private_apartment_address_en__district_en__district_en', 
        lookup_expr='in', method='filter_districts'
    )

    def filter_parent_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)



    class Meta: 
        model = Private_Appartment_EN
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'number_of_rooms', 'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]





class Private_Appartment_RU_Filter(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_private_apartment_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_private_apartment_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_private_apartment_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_private_apartment_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_private_apartment_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_private_apartment_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_private_apartment_name__status',
        choices = Private_Appartment_Names.STATUS_CHOICES
    )
    

    number_of_rooms = filters.MultipleChoiceFilter(
        field_name='internal_private_apartment_name__number_of_rooms', 
        choices=Private_Appartment_Names.NUMBER_OF_ROOM_CHOICES
    )

    city = filters.CharFilter(field_name='private_apartment_address_ru__city_ru__city_ru', lookup_expr='icontains')

    parent_districts = CharInFilter(
        field_name='private_apartment_address_ru__pharentDistrict_ru__pharentDistrict_ru', 
        lookup_expr='in', method='filter_parent_districts'
    )
    districts = CharInFilter(
        field_name='private_apartment_address_ru__district_ru__district_ru', 
        lookup_expr='in', method='filter_districts'
    )


    def filter_parent_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    class Meta: 
        model = Private_Appartment_RU
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'number_of_rooms', 'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]



# ------------------------------------------ground filters   --------------------------------------------------------------------------



class Ground_KA_Filters(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_ground_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_ground_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_ground_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_ground_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_ground_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_ground_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_ground_name__status',
        choices = Ground_Names.STATUS_CHOICES
    )
    

    city = filters.CharFilter(field_name='ground_address_ka__city_ka__city_ka', lookup_expr='icontains')

    parent_districts = CharInFilter(
        field_name='ground_address_ka__pharentDistrict_ka__pharentDistrict_ka', 
        lookup_expr='in', method='filter_parent_districts'
    )
    districts = CharInFilter(
        field_name='ground_address_ka__district_ka__district_ka', 
        lookup_expr='in', method='filter_districts'
    )


    def filter_parent_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    class Meta: 
        model = Ground_KA
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]






class Ground_EN_Filters(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_ground_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_ground_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_ground_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_ground_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_ground_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_ground_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_ground_name__status',
        choices = Ground_Names.STATUS_CHOICES
    )
    

    city = filters.CharFilter(field_name='ground_address_en__city_en__city_en', lookup_expr='icontains')

    parent_districts = CharInFilter(
        field_name='ground_address_en__pharentDistrict_en__pharentDistrict_en', 
        lookup_expr='in', method='filter_parent_districts'
    )
    districts = CharInFilter(
        field_name='ground_address_en__district_en__district_en', 
        lookup_expr='in', method='filter_districts'
    )


    def filter_parent_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    class Meta: 
        model = Ground_EN
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]




class Ground_RU_Filters(filters.FilterSet):
    min_area = filters.NumberFilter(field_name='internal_ground_name__area' , lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='internal_ground_name__area' , lookup_expr='lte')

    min_full_price = filters.NumberFilter(field_name='internal_ground_name__full_price', lookup_expr='gte')
    max_full_price = filters.NumberFilter(field_name='internal_ground_name__full_price', lookup_expr='lte')

    min_square_price= filters.NumberFilter(field_name="internal_ground_name__square_price", lookup_expr='gte')
    max_square_price= filters.NumberFilter(field_name="internal_ground_name__square_price", lookup_expr='lte')

    
    status = filters.MultipleChoiceFilter(
        field_name = 'internal_ground_name__status',
        choices = Ground_Names.STATUS_CHOICES
    )
    

    city = filters.CharFilter(field_name='ground_address_ru__city_ru__city_ru', lookup_expr='icontains')

    parent_districts = CharInFilter(
        field_name='ground_address_ru__pharentDistrict_ru__pharentDistrict_ru', 
        lookup_expr='in', method='filter_parent_districts'
    )
    districts = CharInFilter(
        field_name='ground_address_ru__district_ru__district_ru', 
        lookup_expr='in', method='filter_districts'
    )


    def filter_parent_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    def filter_districts(self, queryset, name, values):
        if not values:
            return queryset
        filter_query = Q()
        for item in values:
            filter_query |= Q(**{f"{name}__icontains": item})
        return queryset.filter(filter_query)

    class Meta: 
        model = Ground_RU
        fields = [
            'min_area', 'max_area', 'min_full_price', 'max_full_price', 
            'min_square_price', 'max_square_price', 
            "status", 'city', 'parent_districts', 'districts'
        ]





# fartis filtracia, 
# fasi - kvadratulze da mtlianad 
# statusi ---   sasofrlo-sameurneo , samosaxlo , komerciuli , 

# ranki undat
        

# sortirebebi :

# damatebis  tarigis mixedvit, mtliani fasis mixedvit , kvadratulis fasis mixedvit , 



