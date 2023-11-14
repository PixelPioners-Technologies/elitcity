from django.db import models
from city_locations.models import CityLocations


class Complex(models.Model):
    # complex_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    price_per_sq_meter = models.DecimalField(max_digits=10, decimal_places=2)
    finished = models.BooleanField()
    space = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_apartments = models.IntegerField()
    number_of_houses = models.IntegerField()
    number_of_floors = models.IntegerField()
    # company_name = models.CharField(max_length=255)  ---->> maybe this hould be foreign key of company table
    phone_number = models.CharField(max_length=20)
    city_location = models.ForeignKey(CityLocations , on_delete=models.CASCADE , related_name='locations' )
    # here should be the planning table's foreign key
    plot_area = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_roof = models.CharField(max_length=100)
    # other fields will be added here

    def __str__(self):
        return self.name

class ComplexImage(models.Model):
    complex = models.ForeignKey(Complex, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
