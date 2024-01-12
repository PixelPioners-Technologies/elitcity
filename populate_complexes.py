# import os
# import django
# from faker import Faker
# import random

# from complex.models import City_KA ,City_EN, City_RU , Language , Address_KA , Address_EN ,Address_RU ,Company_Names ,Company_Images , Company_KA, Company_EN,\
# Company_RU, Complex_Names,Complex_Names ,Complex_Images ,Complex_EN ,Complex_KA ,Complex_RU 

# from complex.models import *

# Adjust the following line according to your project setup
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elitcity.settings')


# django.setup()

# fake = Faker()
# from django.core.management.base import BaseCommand
# from complex.models import *

# # class Command(BaseCommand):
# #     help = 'Populates the database with fake complex data'

# #     def handle(self, *args, **options):
# #         fake = Faker()


# def create_cities():
# for _ in range(5):
#     city_name = fake.city()
#     City_KA.objects.get_or_create(city_ka=city_name)
#     City_EN.objects.get_or_create(city_en=city_name)
#     City_RU.objects.get_or_create(city_ru=city_name)

# def create_addresses():
# for city in City_KA.objects.all():
#     Address_KA.objects.get_or_create(
#         city_ka=city,
#         defaults={
#             'address_ka': fake.street_address(),
#             'longitude': fake.longitude(),
#             'latitude': fake.latitude(),
#         }
#     )

# for city in City_EN.objects.all():
#     Address_EN.objects.get_or_create(
#         city_en=city,
#         defaults={
#             'address_en': fake.street_address(),
#             'longitude': fake.longitude(),
#             'latitude': fake.latitude(),
#         }
#     )

# for city in City_RU.objects.all():
#     Address_RU.objects.get_or_create(
#         city_ru=city,
#         defaults={
#             'address_ru': fake.street_address(),
#             'longitude': fake.longitude(),
#             'latitude': fake.latitude(),
#         }
#     )

# def create_companies():
# for _ in range(5):
#     company_name = fake.company()
#     company = Company_Names.objects.create(
#         internal_name=company_name,
#         Mobile=fake.phone_number(),
#         Mobile_Home=fake.phone_number(),
#         email=fake.email(),
#         companyweb=fake.url(),
#         facebook_page=fake.url(),
#         topCompany=random.choice([True, False]),
#         visibility=random.choice([True, False]),
#     )
#     Company_Images.objects.create(
#         internal_name=company,
#         logocompany=None,  # Add logic to upload an image or leave it as None
#         background_image=None,  # Add logic to upload an image or leave it as None
#     )
#     Company_KA.objects.create(
#         internal_name=company,
#         name_ka=company_name,
#         address_ka=fake.address(),
#         aboutcompany_ka=fake.text(),
#     )
#     Company_EN.objects.create(
#         internal_name=company,
#         name_en=company_name,
#         address_en=fake.address(),
#         aboutcompany_en=fake.text(),
#     )
#     Company_RU.objects.create(
#         internal_name=company,
#         name_ru=company_name,
#         address_ru=fake.address(),
#         aboutcompany_ru=fake.text(),
#     )

# def create_complexes():
# for _ in range(5):
#     complex_name = fake.company_suffix()
#     complex = Complex_Names.objects.create(
#         internal_complex_name=complex_name,
#         full_price=fake.random_number(digits=8),
#         price_per_sq_meter=fake.random_number(digits=6),
#         finish_year=fake.year(),
#         finish_month=fake.month(),
#         status=random.choice([1, 2, 3]),
#         visibiliti=True,
#         vipComplex=random.choice([True, False]),
#         floor_number=fake.random_digit_not_null(),
#         space=fake.random_number(digits=5),
#         number_of_apartments=fake.random_digit_not_null(),
#         number_of_houses=fake.random_digit_not_null(),
#         number_of_floors=fake.random_digit_not_null(),
#         complex_level=fake.random_digit_not_null(),
#         phone_number=fake.phone_number(),
#         plot_area=fake.random_number(digits=5),
#         rank=random.choice(['A', 'B', 'C', 'D', 'E']),
#     )
#     Complex_Images.objects.create(
#         internal_complex_name=complex,
#         images=None,  # Add logic to upload an image or leave it as None
#     )
#     for lang in Language.objects.all():
#         if lang.language == 'EN':
#             Complex_EN.objects.create(
#                 internal_complex_name=complex,
#                 complex_images=complex.images.first(),
#                 company_en=Company_EN.objects.order_by('?').first(),
#                 address_en=Address_EN.objects.order_by('?').first(),
#                 complex_name_en=complex_name,
#                 type_of_roof_en=fake.word(),
#             )
#         elif lang.language == 'KA':
#             Complex_KA.objects.create(
#                 internal_complex_name=complex,
#                 complex_images=complex.images.first(),
#                 company_ka=Company_KA.objects.order_by('?').first(),
#                 address_ka=Address_KA.objects.order_by('?').first(),
#                 complex_name_ka=complex_name,
#                 type_of_roof_ka=fake.word(),
#             )
#         elif lang.language == 'RU':
#             Complex_RU.objects.create(
#                 internal_complex_name=complex,
#                 complex_images=complex.images.first(),
#                 company_ru=Company_RU.objects.order_by('?').first(),
#                 address_ru=Address_RU.objects.order_by('?').first(),
#                 complex_name_ru=complex_name,
#                 type_of_roof_ru=fake.word(),
#             )




# # Call the functions
# create_languages()
# create_cities()
# create_addresses()
# create_companies()
# create_complexes(2)
