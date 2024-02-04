from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Language(models.Model):
    language = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.language
'''
-----------------------------------------------------------------------
            CITY MODELS
-----------------------------------------------------------------------
'''     
class City_KA(models.Model):
    city_ka = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.city_ka
    
class City_EN(models.Model):
    city_en = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.city_en

class City_RU(models.Model):
    city_ru = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.city_ru
'''
-----------------------------------------------------------------------
            PHERENTDISTRICT MODELS
-----------------------------------------------------------------------
''' 
class PharentDistrict_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE, related_name='pharentDistrict_ka')
    pharentDistrict_ka = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ka.city_ka} - {self.pharentDistrict_ka}"
    

class PharentDistrict_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE,related_name='pharentDistrict_en')
    pharentDistrict_en = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_en.city_en} - {self.pharentDistrict_en}"
    
class PharentDistrict_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE, related_name='pharentDistrict_ru')
    pharentDistrict_ru = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ru.city_ru} - {self.pharentDistrict_ru}"
'''
-----------------------------------------------------------------------
            DISTRICT MODELS
-----------------------------------------------------------------------
''' 
class District_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE, related_name='district_ka')
    pharentDistrict_ka = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE,related_name='district_ka')
    district_ka = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ka.city_ka} - {self.pharentDistrict_ka.pharentDistrict_ka} - {self.district_ka}"

class District_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE,related_name='district_en')
    pharentDistrict_en = models.ForeignKey(PharentDistrict_EN, on_delete=models.CASCADE,related_name='district_en')
    district_en = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_en.city_en} - {self.pharentDistrict_en.pharentDistrict_en} - {self.district_en}"
    
class District_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE, related_name='district_ru')
    pharentDistrict_ru = models.ForeignKey(PharentDistrict_RU, on_delete=models.CASCADE, related_name='district_ru')
    district_ru = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ru.city_ru} - {self.pharentDistrict_ru.pharentDistrict_ru} - {self.district_ru}"
'''
-----------------------------------------------------------------------
            STREET_NAME MODELS
-----------------------------------------------------------------------
''' 
class Street_Name_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE)
    pharentDistrict_ka = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE)
    district_ka = models.ForeignKey(District_KA, on_delete=models.CASCADE)
    street_name_ka = models.CharField(max_length=50)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ka.city_ka} - {self.pharentDistrict_ka.pharentDistrict_ka} - {self.district_ka.district_ka} - {self.street_name_ka}" 

class Street_Name_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE)
    pharentDistrict_en = models.ForeignKey(PharentDistrict_EN, on_delete=models.CASCADE)
    district_en = models.ForeignKey(District_EN, on_delete=models.CASCADE)
    street_name_en = models.CharField(max_length=50)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_en.city_en} - {self.pharentDistrict_en.pharentDistrict_en} - {self.district_en.district_en} - {self.street_name_en}" 
    
class Street_Name_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE)
    pharentDistrict_ru = models.ForeignKey(PharentDistrict_RU, on_delete=models.CASCADE)
    district_ru = models.ForeignKey(District_RU, on_delete=models.CASCADE)
    street_name_ru = models.CharField(max_length=50)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ru.city_ru} - {self.pharentDistrict_ru.pharentDistrict_ru} - {self.district_ru.district_ru} - {self.street_name_ru}" 
'''
-----------------------------------------------------------------------
            ADDRESS MODELS
-----------------------------------------------------------------------
''' 
class Address_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE, blank=True, null=True)
    pharentDistrict_ka = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE, blank=True, null=True)
    district_ka = models.ForeignKey(District_KA, on_delete=models.CASCADE, blank=True, null=True)
    street_name_ka = models.ForeignKey(Street_Name_KA, on_delete=models.CASCADE, blank=True, null=True)
    address_ka = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ka.city_ka} - {self.pharentDistrict_ka.pharentDistrict_ka} - {self.district_ka.district_ka} - {self.street_name_ka.street_name_ka} - {self.address_ka}"

class Address_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE, blank=True, null=True)
    pharentDistrict_en = models.ForeignKey(PharentDistrict_EN, on_delete=models.CASCADE, blank=True, null=True)
    district_en = models.ForeignKey(District_EN, on_delete=models.CASCADE, blank=True, null=True)
    street_name_en = models.ForeignKey(Street_Name_EN, on_delete=models.CASCADE, blank=True, null=True)
    address_en = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_en.city_en} - {self.pharentDistrict_en.pharentDistrict_en} - {self.district_en.district_en} - {self.street_name_en.street_name_en} - {self.address_en}"
    
class Address_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE, blank=True, null=True)
    pharentDistrict_ru = models.ForeignKey(PharentDistrict_RU, on_delete=models.CASCADE, blank=True, null=True)
    district_ru = models.ForeignKey(District_RU, on_delete=models.CASCADE, blank=True, null=True)
    street_name_ru = models.ForeignKey(Street_Name_RU, on_delete=models.CASCADE, blank=True, null=True)
    address_ru = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ru.city_ru} - {self.pharentDistrict_ru.pharentDistrict_ru} - {self.district_ru.district_ru} - {self.street_name_ru.street_name_ru} - {self.address_ru}"
'''
-----------------------------------------------------------------------
            COMPANY MODELS
-----------------------------------------------------------------------
''' 
class Company_Names(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    internal_name = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=20)
    Mobile_Home = models.CharField(max_length=20)
    email = models.EmailField()
    companyweb = models.URLField(max_length=200, blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    topCompany = models.BooleanField(default=False)
    visibility = models.BooleanField(default=True)
    def __str__(self):
        return self.internal_name
    
class Company_Images(models.Model):
    internal_name = models.ForeignKey(Company_Names, on_delete=models.CASCADE)
    logocompany = models.ImageField(upload_to='company_logos/', blank=True, null=True, )#unique=True
    background_image = models.ImageField(upload_to='company_background_images/', blank=True, null=True) #unique=True
    def __str__(self):
        return self.internal_name.internal_name

class Company_KA(models.Model):
    internal_name = models.ForeignKey(Company_Images, on_delete=models.CASCADE)
    name_ka = models.CharField(max_length=255)
    address_ka = models.TextField()
    aboutcompany_ka = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_ka

class Company_EN(models.Model):
    internal_name = models.ForeignKey(Company_Images, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=255)
    address_en = models.TextField()
    aboutcompany_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_en
    
class Company_RU(models.Model):
    internal_name = models.ForeignKey(Company_Images, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=255)
    address_ru = models.TextField()
    aboutcompany_ru = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_ru
'''
-----------------------------------------------------------------------
            COMPLEX MODELS
-----------------------------------------------------------------------
''' 


class ComplexStatus(models.IntegerChoices):
    PLANNED = 1, 'Planned'
    UNDER_CONSTRUCTION = 2, 'Under Construction'
    COMPLETED = 3, 'Completed'



class Complex_Names(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    internal_complex_name = models.CharField(max_length=255, unique=True)
    full_price = models.DecimalField(max_digits = 8 , decimal_places=2 , null=True , blank=True)
    price_per_sq_meter = models.DecimalField(max_digits=10, decimal_places=2)
    finish_year = models.IntegerField(blank=True,null=True)
    finish_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True,null=True)
    status = models.IntegerField(choices=ComplexStatus.choices, default=ComplexStatus.UNDER_CONSTRUCTION)
    visibiliti = models.BooleanField(default=True)
    vipComplex = models.BooleanField(default=False)
    floor_number = models.IntegerField()
    space = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_apartments = models.IntegerField()
    number_of_floors = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    # for information fields - integer da float fields aq davtove, Boolean - ebs qvemot davamateb
    number_of_buildings = models.IntegerField( blank=True,null=True)
    flooring = models.IntegerField(blank=True,null=True)
    parking_quantity = models.IntegerField( blank=True,null=True)
    rooms_quantity = models.IntegerField(blank=True,null=True)
    light_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True,null=True)
    humidity_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True,null=True)
    area_squareness = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    ceiling_height_meters = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
    catering_facility = models.BooleanField(default=True)
    elevator_type = models.BooleanField(default=True)
    schlangbaum = models.BooleanField(default=True)
    concierge_service = models.BooleanField(default=True)
    yard_description = models.BooleanField(default=True)

    views_count = models.IntegerField(default=0)

   
    plot_area = models.DecimalField(max_digits=10, decimal_places=2) # am fildze savaraudod unda gaketdes fartis filtracia , da kvadratulobis filtracia albat iqneba apartmentebze
    RANK_CHOICES = [
        ('A', 'Rank A'),
        ('B', 'Rank B'),
        ('C', 'Rank C'),
        ('D', 'Rank D'),
        ('E', 'Rank E'),
    ]

    rank = models.CharField(max_length=1, choices=RANK_CHOICES, default='E')

    def __str__(self):
        return self.internal_complex_name
    
class Complex_Images(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Names,  on_delete=models.CASCADE)
    images = models.ImageField(upload_to='complex_images/')
    def __str__(self):
        return self.internal_complex_name.internal_complex_name
    
class Complex_KA(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Names, on_delete=models.CASCADE)
    complex_images = models.ForeignKey(Complex_Images, on_delete=models.CASCADE)
    company_ka = models.ForeignKey(Company_KA, on_delete=models.CASCADE, null=True, blank=True)
    address_ka = models.ForeignKey(Address_KA, on_delete=models.CASCADE)
    complex_name_ka = models.CharField(max_length=200, unique=True)
    type_of_roof_ka = models.CharField(max_length=100)

    construction_type_ka = models.CharField(max_length=100,null=True, blank=True)
    submission_type_ka = models.CharField(max_length=100,null=True, blank=True)
    protection_type_ka = models.CharField(max_length=100,null=True, blank=True)
    metro_ka = models.CharField(max_length=50 ,null=True, blank=True)
    Pharmacy_ka = models.CharField(max_length=50,null=True, blank=True)
    supermarket_ka = models.CharField(max_length=50,null=True, blank=True)
    Square_ka = models.CharField(max_length=50,null=True, blank=True)
    Description_ka = models.TextField(max_length=500,null=True, blank=True)

    
    def __str__(self):
        return self.internal_complex_name.internal_complex_name
    
class Complex_EN(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Names, on_delete=models.CASCADE)
    complex_images = models.ForeignKey(Complex_Images, on_delete=models.CASCADE)
    company_en = models.ForeignKey(Company_EN, on_delete=models.CASCADE, null=True, blank=True)
    address_en = models.ForeignKey(Address_EN, on_delete=models.CASCADE)
    complex_name_en = models.CharField(max_length=200, unique=True)
    type_of_roof_en = models.CharField(max_length=100)

    construction_type_en = models.CharField(max_length=100,null=True, blank=True)
    submission_type_en = models.CharField(max_length=100,null=True, blank=True)
    protection_type_en = models.CharField(max_length=100,null=True, blank=True)
    metro_en = models.CharField(max_length=50,null=True, blank=True)
    Pharmacy_en = models.CharField(max_length=50,null=True, blank=True)
    supermarket_en = models.CharField(max_length=50,null=True, blank=True)
    Square_en = models.CharField(max_length=50,null=True, blank=True)
    Description_en = models.TextField(max_length=500,null=True, blank=True)


    
    def __str__(self):
        return self.internal_complex_name.internal_complex_name
    
class Complex_RU(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Names, on_delete=models.CASCADE)
    complex_images = models.ForeignKey(Complex_Images, on_delete=models.CASCADE)
    company_ru = models.ForeignKey(Company_RU, on_delete=models.CASCADE, null=True, blank=True)
    address_ru = models.ForeignKey(Address_RU, on_delete=models.CASCADE)
    complex_name_ru = models.CharField(max_length=200, unique=True)
    type_of_roof_ru = models.CharField(max_length=100)

    construction_type_ru = models.CharField(max_length=100,null=True, blank=True)
    submission_type_ru = models.CharField(max_length=100,null=True, blank=True)
    protection_type_ru = models.CharField(max_length=100,null=True, blank=True)
    metro_ru = models.CharField(max_length=50,null=True, blank=True)
    Pharmacy_ru = models.CharField(max_length=50,null=True, blank=True)
    supermarket_ru = models.CharField(max_length=50,null=True, blank=True)
    Square_ru = models.CharField(max_length=50,null=True, blank=True)
    Description_ru = models.TextField(max_length=500,null=True, blank=True)



    def __str__(self):
        return self.internal_complex_name.internal_complex_name

'''
-----------------------------------------------------------------------
            APPARTMENT MODELS
-----------------------------------------------------------------------
''' 
class Appartment_Names(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    complex = models.ForeignKey(Complex_Names, on_delete=models.CASCADE, null=True, blank=True, related_name='appartment_names')
    internal_apartment_name = models.CharField(max_length=50)
    NUMBER_OF_ROOM_CHOICES = [
        ('studio', 'Studio'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5+', '5+'),
    ]
    STATUS_CHOICES=[
        ("1" , 'Newly renovated'),
        ('2' , 'with old repairs'),
        ('3', 'to be repaired'),
    ]
    number_of_rooms = models.CharField( 
        max_length =10,
        choices = NUMBER_OF_ROOM_CHOICES,
        default="studio"
     )
    status = models.CharField(
        max_length = 30,
        choices = STATUS_CHOICES,
        default = "3"
    )
    area = models.DecimalField(max_digits=7, decimal_places=2)
    full_price = models.DecimalField(max_digits=12, decimal_places=2)
    square_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True )
    floor_number = models.IntegerField()
    is_available = models.BooleanField(default=True)
    visibiliti = models.BooleanField(default=True)

    metro = models.BooleanField(default=True , blank=True , null = True)
    Pharmacy = models.BooleanField(default=True , blank=True , null = True)
    supermarket = models.BooleanField(default=True , blank=True , null = True)
    square = models.BooleanField(default=True , blank=True , null = True)

    
    def __str__(self):
        return f"{self.internal_apartment_name}"

    
class Appartment_Images(models.Model):
    internal_apartment_name = models.ForeignKey(Appartment_Names,  on_delete=models.CASCADE)
    images = models.ImageField(upload_to='apartment_images/')

    def __str__(self):
        return f"{self.internal_apartment_name.internal_apartment_name}"


class Appartment_KA(models.Model):
    internal_apartment_name = models.ForeignKey(Appartment_Names,  on_delete=models.CASCADE)
    complex_ka = models.ForeignKey(Complex_KA, on_delete=models.CASCADE, null=True, related_name='appartment_name_ka')
    appartment_name_ka = models.CharField(max_length=100,null=True)
    appartment_images = models.ForeignKey(Appartment_Images, on_delete = models.CASCADE, null=True)
    appartment_address_ka = models.ForeignKey(Address_KA, on_delete = models.CASCADE,null = True)
    test_field_ka = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.internal_apartment_name.internal_apartment_name}"


class Appartment_EN(models.Model):
    internal_apartment_name = models.ForeignKey(Appartment_Names,  on_delete=models.CASCADE)
    complex_en = models.ForeignKey(Complex_EN, on_delete=models.CASCADE,null=True, related_name='appartment_name_en')
    appartment_name_en = models.CharField(max_length=100,null=True)
    appartment_images = models.ForeignKey(Appartment_Images, on_delete = models.CASCADE, null=True)
    appartment_address_en = models.ForeignKey(Address_EN, on_delete = models.CASCADE, null = True)
    test_field_en = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.internal_apartment_name.internal_apartment_name}"



    
class Appartment_RU(models.Model):
    internal_apartment_name = models.ForeignKey(Appartment_Names,  on_delete=models.CASCADE)
    complex_ru = models.ForeignKey(Complex_RU, on_delete=models.CASCADE,null=True, related_name='appartment_name_ru')
    appartment_name_ru = models.CharField(max_length=100,null=True)
    appartment_images = models.ForeignKey(Appartment_Images, on_delete = models.CASCADE, null=True)
    appartment_address_ru = models.ForeignKey(Address_RU, on_delete = models.CASCADE,null = True)
    test_field_ru = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.internal_apartment_name.internal_apartment_name}"



'''
-----------------------------------------------------------------------
           PRIVATE  APPARTMENT MODELS
-----------------------------------------------------------------------
''' 
class Private_Appartment_Names(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    internal_private_apartment_name = models.CharField(max_length=50)
    NUMBER_OF_ROOM_CHOICES = [
        ('studio', 'Studio'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5+', '5+'),
    ]
    STATUS_CHOICES=[
        ("1" , 'Newly renovated'),
        ('2' , 'with old repairs'),
        ('3', 'to be repaired'),
    ]
    number_of_rooms = models.CharField(
        max_length=10,
        choices = NUMBER_OF_ROOM_CHOICES,
        default = "studio"
    )
    status = models.CharField(
        max_length = 30,
        choices = STATUS_CHOICES,
        default = "3",
    )
    RANK_CHOICES = [
        ('A', 'Rank A'),
        ('B', 'Rank B'),
        ('C', 'Rank C'),
        ('D', 'Rank D'),
        ('E', 'Rank E'),
    ]

    rank = models.CharField(max_length=1, choices=RANK_CHOICES, default='E')

    area = models.DecimalField(max_digits=7, decimal_places=2)
    full_price = models.DecimalField(max_digits=12, decimal_places=2)
    square_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    floor_number = models.IntegerField()
    is_available = models.BooleanField(default=True)
    visibiliti = models.BooleanField(default=True)

        
    def __str__(self):
        return f"{self.internal_private_apartment_name}"


    
class Private_Appartment_images(models.Model):
    internal_private_apartment_name = models.ForeignKey(Private_Appartment_Names,  on_delete=models.CASCADE)
    images = models.ImageField(upload_to='private_apartment_images/')

    def __str__(self):
        return f"{self.internal_private_apartment_name.internal_private_apartment_name}"


class Private_Appartment_EN(models.Model):
    internal_private_apartment_name = models.ForeignKey(Private_Appartment_Names ,on_delete=models.CASCADE)
    private_apartment_images = models.ForeignKey(Private_Appartment_images, on_delete = models.CASCADE, null=True)
    private_apartment_address_en = models.ForeignKey(Address_EN, on_delete = models.CASCADE,null = True)
    private_apartment_name_en = models.CharField(max_length=100,null=True)
    test_private_field_en = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.private_apartment_name_en} - {self.internal_private_apartment_name}"



class Private_Appartment_KA(models.Model):
    internal_private_apartment_name = models.ForeignKey(Private_Appartment_Names ,on_delete=models.CASCADE)
    private_apartment_images = models.ForeignKey(Private_Appartment_images, on_delete = models.CASCADE, null=True)
    private_apartment_address_ka = models.ForeignKey(Address_KA, on_delete = models.CASCADE,null = True)
    private_apartment_name_ka = models.CharField(max_length=100,null=True)
    test_private_field_ka = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.private_apartment_name_ka} - {self.internal_private_apartment_name}"

class Private_Appartment_RU(models.Model):
    internal_private_apartment_name = models.ForeignKey(Private_Appartment_Names ,on_delete=models.CASCADE)
    private_apartment_images = models.ForeignKey(Private_Appartment_images, on_delete = models.CASCADE, null=True)
    private_apartment_address_ru = models.ForeignKey(Address_RU, on_delete = models.CASCADE,null = True)
    private_apartment_name_ru = models.CharField(max_length=100,null=True)
    test_private_field_ru = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.private_apartment_name_ru} - {self.internal_private_apartment_name}"


'''
-----------------------------------------------------------------------
            GROUND MODELS
-----------------------------------------------------------------------
''' 


class Ground_Names(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    internal_ground_name = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=12, decimal_places=2)
    full_price = models.DecimalField(max_digits=12, decimal_places=2)
    square_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_available = models.BooleanField(default=True)
    visibiliti = models.BooleanField(default=True)
    STATUS_CHOICES = [
        ("1" , 'Agricultural'),
        ('2' , 'Land for settlement'),
        ('3', 'Commercial'),
    ]
    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = "3",
    )
    RANK_CHOICES = [
        ('A', 'Rank A'),
        ('B', 'Rank B'),
        ('C', 'Rank C'),
        ('D', 'Rank D'),
        ('E', 'Rank E'),
    ]
    
    rank = models.CharField(max_length=1, choices=RANK_CHOICES, default='E')

    
    def __str__(self):
        return f"{self.internal_ground_name}"

    
class Ground_Images(models.Model):
    internal_ground_name = models.ForeignKey(Ground_Names,  on_delete=models.CASCADE)
    images = models.ImageField(upload_to='ground_images/')

    def __str__(self):
        return f"{self.internal_ground_name.internal_ground_name}"


class Ground_KA(models.Model):
    internal_ground_name = models.ForeignKey(Ground_Names,  on_delete=models.CASCADE)
    ground_name_ka = models.CharField(max_length=100, null=True)
    ground_images = models.ForeignKey(Ground_Images, on_delete = models.CASCADE, blank=True, null=True)
    ground_address_ka = models.ForeignKey(Address_KA, on_delete = models.CASCADE, blank=True, null=True)
    
    
class Ground_EN(models.Model):
    internal_ground_name = models.ForeignKey(Ground_Names,  on_delete=models.CASCADE)
    ground_name_en = models.CharField(max_length=100,null=True)
    ground_images = models.ForeignKey(Ground_Images, on_delete = models.CASCADE, blank=True, null=True)
    ground_address_en = models.ForeignKey(Address_EN, on_delete = models.CASCADE, blank=True, null=True)
    

    
class Ground_RU(models.Model):
    internal_ground_name = models.ForeignKey(Ground_Names,  on_delete=models.CASCADE)
    ground_name_ru = models.CharField(max_length=100,null=True)
    ground_images = models.ForeignKey(Ground_Images, on_delete = models.CASCADE, blank=True, null=True)
    ground_address_ru = models.ForeignKey(Address_RU, on_delete = models.CASCADE, blank=True, null=True)


'''
-----------------------------------------------------------------------
            BLOG MODELS
-----------------------------------------------------------------------
''' 


class Blog_Names(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Blog_Images(models.Model):
    internal_blog_name = models.ForeignKey(Blog_Names, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"{self.internal_blog_name.title}"

class Blog_KA(models.Model):
    internal_blog_name = models.ForeignKey(Blog_Names, on_delete=models.CASCADE)
    blog_name_ka = models.CharField(max_length=100, null=True)
    blog_images = models.ForeignKey(Blog_Images, on_delete = models.CASCADE, blank=True, null=True)

class Blog_EN(models.Model):
    internal_blog_name = models.ForeignKey(Blog_Names, on_delete=models.CASCADE)
    blog_name_en = models.CharField(max_length=100, null=True)
    blog_images = models.ForeignKey(Blog_Images, on_delete = models.CASCADE, blank=True, null=True)

class Blog_RU(models.Model):
    internal_blog_name = models.ForeignKey(Blog_Names, on_delete=models.CASCADE)
    blog_name_ru = models.CharField(max_length=100, null=True)
    blog_images = models.ForeignKey(Blog_Images, on_delete = models.CASCADE, blank=True, null=True)
    

'''
-----------------------------------------------------------------------
            PROMOTIONS AND OFFERS
-----------------------------------------------------------------------
''' 

class Promotions_and_offers_Names(models.Model):
    internal_promotion_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.ForeignKey(Company_Names, on_delete=models.CASCADE)
    discount = models.BooleanField(default=True)
    gift = models.BooleanField(default=True)
    installment = models.BooleanField(default=False)
    visibility = models.BooleanField(default=True)


    def __str__(self):
        return self.internal_promotion_name


class Promotions_and_offers_Images(models.Model):
    internal_promotion_name = models.ForeignKey(Promotions_and_offers_Names, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='promotions_images/')

    def __str__(self):
        return f"{self.internal_promotion_name.internal_promotion_name}"


class Promotions_and_offers_KA(models.Model):
    internal_promotion_name = models.ForeignKey(Promotions_and_offers_Names, on_delete=models.CASCADE)
    promotion_name_ka = models.CharField(max_length=255, null=True)
    promotion_images = models.ForeignKey(Promotions_and_offers_Images, on_delete=models.CASCADE, blank=True, null=True)
    about_ka = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.promotion_name_ka

class Promotions_and_offers_EN(models.Model):
    internal_promotion_name = models.ForeignKey(Promotions_and_offers_Names, on_delete=models.CASCADE)
    promotion_name_en = models.CharField(max_length=255, null=True)
    promotion_images = models.ForeignKey(Promotions_and_offers_Images, on_delete=models.CASCADE, blank=True, null=True)
    about_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.promotion_name_en


class Promotions_and_offers_RU(models.Model):
    internal_promotion_name = models.ForeignKey(Promotions_and_offers_Names, on_delete=models.CASCADE)
    promotion_name_ru = models.CharField(max_length=255, null=True)
    promotion_images = models.ForeignKey(Promotions_and_offers_Images, on_delete=models.CASCADE, blank=True, null=True)
    about_ru = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.promotion_name_ru