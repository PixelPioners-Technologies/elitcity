from django.db import models


    
class City(models.Model):
    city_ka = models.CharField(max_length=50, unique=True)
    city_en = models.CharField(max_length=50, unique=True)
    city_ru = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.city_ka

class PharentDistrict(models.Model):
    city_ka = models.ForeignKey(City, on_delete=models.CASCADE, related_name="pharent_districts_ka")
    city_en = models.ForeignKey(City, on_delete=models.CASCADE, related_name="pharent_districts_en")
    city_ru = models.ForeignKey(City, on_delete=models.CASCADE, related_name="pharent_districts_ru")
    pharentDistrict_ka = models.CharField(max_length=50, unique=True)
    pharentDistrict_en = models.CharField(max_length=50, unique=True)
    pharentDistrict_eu = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.pharentDistrict_ka

class Lang(models.Model):
    language = models.CharField(max_length=2, unique=True)
    cities = models.ManyToManyField(City, related_name='langs')
    pharentDistrict = models.ManyToManyField(PharentDistrict, related_name="pharent_dist")

    def __str__(self):
        return self.language
    

    
# class District(models.Model):
#     city_ka = models.ForeignKey(City, on_delete=models.CASCADE, related_name="districts_ka")
#     city_en = models.ForeignKey(City, on_delete=models.CASCADE, related_name="districts_en")
#     city_ru = models.ForeignKey(City, on_delete=models.CASCADE, related_name="districts_ru")
#     pharentDistrict_ka = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="districts_pharent_ka")
#     pharentDistrict_en = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="districts_pharent_en")
#     pharentDistrict_ru = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="districts_pharent_ru")
#     district_ka = models.CharField(max_length=200, unique=True)
#     district_en = models.CharField(max_length=200, unique=True)
#     district_ru = models.CharField(max_length=200, unique=True)
#     def __str__(self):
#         return self.district_ka
    
# class DirectAddress(models.Model):
#     city_ka = models.ForeignKey(City, on_delete=models.CASCADE, related_name="direct_addresses_ka")
#     city_en = models.ForeignKey(City, on_delete=models.CASCADE, related_name="direct_addresses_en")
#     city_ru = models.ForeignKey(City, on_delete=models.CASCADE, related_name="direct_addresses_ru")
#     pharentDistrict_ka = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="direct_addresses_ka")
#     pharentDistrict_en = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="direct_addresses_en")
#     pharentDistrict_ru = models.ForeignKey(PharentDistrict, on_delete=models.CASCADE, related_name="direct_addresses_ru")
#     district_ka = models.ForeignKey(District, on_delete=models.CASCADE, related_name="direct_addresses_ka")
#     district_en = models.ForeignKey(District, on_delete=models.CASCADE, related_name="direct_addresses_en")
#     district_ru = models.ForeignKey(District, on_delete=models.CASCADE, related_name="direct_addresses_eu")
#     street_ka = models.CharField(max_length=200)
#     street_en = models.CharField(max_length=200)
#     street_ru = models.CharField(max_length=200)
#     street_num_ka = models.CharField(max_length=20)
#     street_num_en = models.CharField(max_length=20)
#     street_num_ru = models.CharField(max_length=20)
#     latitude = models.FloatField(default=0.0)
#     longitude = models.FloatField(default=0.0)

#     def __str__(self):
#         return f"{self.street_ka} {self.street_num_ka}"
    
# class Company(models.Model):
#     name_ka = models.CharField(max_length=255, unique=True)
#     name_en = models.CharField(max_length=255, unique=True)
#     name_ru = models.CharField(max_length=255, unique=True)
#     address_ka = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="company_address_ka")
#     address_en = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="company_address_en")
#     address_ru = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="company_address_ru")
#     Mobile = models.CharField(max_length=20)
#     Mobile_Home = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     companyweb = models.URLField(max_length=200, blank=True, null=True)
#     aboutcompany_ka = models.TextField(blank=True, null=True)
#     aboutcompany_en = models.TextField(blank=True, null=True)
#     aboutcompany_ru = models.TextField(blank=True, null=True)
#     logocompany = models.ImageField(upload_to='company_logos/', blank=True, null=True)
#     background_image = models.ImageField(upload_to='company_background_images/', blank=True, null=True)
#     facebook_page = models.URLField(blank=True, null=True)
#     visibility = models.BooleanField()

#     def __str__(self):
#         return self.name_ka
    
# class Complex(models.Model):
#     company_ka = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='complexes_ka')
#     company_en = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='complexes_en')
#     company_ru = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='complexes_ru')
#     name_ka = models.CharField(max_length=255)
#     name_en = models.CharField(max_length=255)
#     name_ru = models.CharField(max_length=255)
#     address_ka = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="complex_ka")
#     address_en = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="complex_en")
#     address_ru = models.ForeignKey(DirectAddress,on_delete=models.CASCADE, related_name="complex_ru")
#     price_per_sq_meter = models.DecimalField(max_digits=10, decimal_places=2)
#     finished = models.BooleanField()
#     space = models.DecimalField(max_digits=10, decimal_places=2)
#     number_of_apartments = models.IntegerField()
#     number_of_houses = models.IntegerField()
#     number_of_floors = models.IntegerField()
#     phone_number = models.CharField(max_length=20)
#     plot_area = models.DecimalField(max_digits=10, decimal_places=2)
#     type_of_roof_ka = models.CharField(max_length=100)
#     type_of_roof_en = models.CharField(max_length=100)
#     type_of_roof_ru = models.CharField(max_length=100)
#     visibility = models.BooleanField()
    
#     def __str__(self):
#         return self.name_ka

# class Apartment(models.Model):
#     complex_ka = models.ForeignKey(Complex, on_delete=models.CASCADE, related_name='apartments_ka')
#     complex_en = models.ForeignKey(Complex, on_delete=models.CASCADE, related_name='apartments_en')
#     complex_ru = models.ForeignKey(Complex, on_delete=models.CASCADE, related_name='apartments_ru')
#     number_of_rooms = models.IntegerField()
#     area = models.DecimalField(max_digits=7, decimal_places=2)
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     floor_number = models.IntegerField()
#     is_available = models.BooleanField(default=True)
#     visibility = models.BooleanField()
    
#     def __str__(self):
#         return f"{self.number_of_rooms} room(s) - {self.area}m² - {self.complex_ka.name_ka}"


# class ComplexImage(models.Model):
#     complex = models.ForeignKey(Complex, related_name='images', on_delete=models.CASCADE)
#     images = models.ImageField(upload_to='complex_images/')
#     def __str__(self):
#         return self.complex.name_ka

# class ApartmentImage(models.Model):
#     apartment = models.ForeignKey(Apartment, related_name='apartment', on_delete=models.CASCADE)
#     images = models.ImageField(upload_to='apartment_images/')
#     def __str__(self):
#         return f"Appartments of {self.apartment.complex_ka.name_ka}"

# class VIPComplex(models.Model):
#     complex = models.OneToOneField(Complex , on_delete=models.CASCADE , related_name='vip_details' )

#     def __str__(self):
#         return self.complex.name_ka
    

# class TopCompany(models.Model):
#     company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='top_company' )

#     def __str__(self):
#         return self.company.name_ka