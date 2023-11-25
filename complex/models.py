from django.db import models
from django.contrib.postgres.fields import ArrayField



class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    Mobile = models.CharField(max_length=20)
    Mobile_Home = models.CharField(max_length=20)
    email = models.EmailField()
    companyweb = models.URLField(max_length=200, blank=True, null=True)
    aboutcompany = models.TextField(blank=True, null=True)
    logocompany = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    background_image = models.ImageField(upload_to='company_background_images/', blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
class PharentDistrict(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="pharent_districts")
    pharentDistrict = models.CharField(max_length=50)

    def __str__(self):
        return self.pharentDistrict
    
class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="districts")
    pharentDistrict = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="districts")
    district = models.CharField(max_length=200)
    def __str__(self):
        return self.district
    
class DirectAddress(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="direct_addresses")
    pharentDistrict = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="direct_addresses")
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="direct_addresses")
    street = models.CharField(max_length=200)
    def __str__(self):
        return self.street
        
class Complex(models.Model):
    company = models.ForeignKey(Company, related_name='complexes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="complex")
    price_per_sq_meter = models.DecimalField(max_digits=10, decimal_places=2)
    finished = models.BooleanField()
    space = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_apartments = models.IntegerField()
    number_of_houses = models.IntegerField()
    number_of_floors = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    plot_area = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_roof = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Apartment(models.Model):
    complex = models.ForeignKey(Complex, related_name='apartments', on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField()
    area = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    floor_number = models.IntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.number_of_rooms} room(s) - {self.area}m² - {self.complex.name}"


class ComplexImage(models.Model):
    complex = models.ForeignKey(Complex, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='complex_images/')
    def __str__(self):
        return self.complex.name
