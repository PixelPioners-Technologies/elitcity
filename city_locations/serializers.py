from rest_framework import serializers
from .models import CityLocations


class CityLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityLocations
        fields = '__all__'