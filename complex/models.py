from django.db import models




class Company(models.Model):

    ''' კომპანიის სახელი ( დასახელება )'''
    name = models.CharField(max_length=255)

    ''' 
    კომპანიის მისამართი. მაგ: ილია ჭავჭავაძის გამზირი # 36 
    '''
    address = models.TextField()
    
    ''' მობილური ტელეფონოის ნომერი, მაგ: 595456545'''
    Mobile = models.CharField(max_length=20)

    ''' სახლის ტელეფონი. მაგ: 03222654854'''
    Mobile_Home = models.CharField(max_length=20)

    ''' ცომპანიის მაილის მისამართი'''
    email = models.EmailField()

    ''' კომპანიის ვებ გვერდის მისამართი (ლინკი)'''
    companyweb = models.URLField(max_length=200, blank=True, null=True)

    ''' კომპანიის შესახებ ტექსტური ინფორმაცია'''
    aboutcompany = models.TextField(blank=True, null=True)

    ''' კომპანიის ლოგო'''
    logocompany = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    ''' კომპანიის background ფოტო'''
    background_image = models.ImageField(upload_to='company_background_images/', blank=True, null=True)

    ''' facebook - ის მისამართი'''
    facebook_page = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name



class Complex(models.Model):
    ''' This ForeignKey establishes a many-to-one relationship between the Complex and Company models
    indicating that each Complex is associated with one Company
    and each Company can be associated with multiple Complex instances '''
    company = models.ForeignKey(Company, related_name='complexes', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    address = models.TextField()
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
    complex = models.ForeignKey(Complex, related_name='test_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='complex_images/')


class VIPComplex(models.Model):
    complex = models.OneToOneField(Complex , on_delete=models.CASCADE , related_name='vip_details' )

    def __str__(self):
        return self.complex.name