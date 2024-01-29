import os
import django
import random
from faker import Faker
from decimal import Decimal, getcontext
from django.utils import timezone
fake = Faker()

created_at = fake.date_time_this_decade()


# getcontext().prec = 8

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elitcity.settings")
django.setup()

from complex.models import *


def add_address_en():
    address_en = fake.street_address()[:30]
    longitude = round(random.uniform(-180, 180), 6)
    latitude = round(random.uniform(-90, 90), 6)
    a = Address_EN.objects.get_or_create(address_en=address_en, longitude=longitude, latitude=latitude)[0]
    a.save()
    return a

def add_address_ka():
    address_ka = fake.street_address()[:30]
    longitude = round(random.uniform(-180, 180), 6)
    latitude = round(random.uniform(-90, 90), 6)
    a = Address_KA.objects.get_or_create(address_ka=address_ka, longitude=longitude, latitude=latitude)[0]
    a.save()
    return a

def add_address_ru():
    address_ru = fake.street_address()[:30]
    longitude = round(random.uniform(-180, 180), 6)
    latitude = round(random.uniform(-90, 90), 6)
    a = Address_RU.objects.get_or_create(address_ru=address_ru, longitude=longitude, latitude=latitude)[0]
    a.save()
    return a

def add_appartment_names():
    created_at = timezone.make_aware(fake.date_time_this_decade(), timezone.get_default_timezone())
    internal_apartment_name = fake.word()[:50]
    number_of_rooms = random.choice(['studio', '1', '2', '3', '4', '5+'])
    status = random.choice(['1', '2', '3'])
    area = Decimal(round(random.uniform(20, 99999.99), 2))
    full_price = Decimal(round(random.uniform(10000, 99999.99), 2))
    square_price = Decimal(full_price / area).quantize(Decimal('.01')) if area > 0 else Decimal(0)
    floor_number = random.randint(1, 50)
    is_available = random.choice([True, False])
    visibiliti = random.choice([True, False])
    
    apartment = Appartment_Names.objects.get_or_create(
        created_at=created_at, 
        internal_apartment_name=internal_apartment_name, 
        number_of_rooms=number_of_rooms,
        status=status, 
        area=area,
        full_price=full_price,
        square_price=square_price,
        floor_number=floor_number,
        is_available=is_available,
        visibiliti=visibiliti
    )[0]
    apartment.save()

def add_company_names():
    internal_name = fake.company()
    Mobile = fake.phone_number()[:20]
    Mobile_Home = fake.phone_number()[:20] 
    email = fake.email()
    # companyweb = fake.url()[:20]
    facebook_page = fake.url()
    topCompany = random.choice([True, False])
    visibility = random.choice([True, False])
    
    company = Company_Names.objects.get_or_create(
        internal_name=internal_name, 
        Mobile=Mobile, 
        Mobile_Home=Mobile_Home,
        email=email, 
        # companyweb=companyweb,
        facebook_page=facebook_page,
        topCompany=topCompany,
        visibility=visibility
    )[0]
    company.save()

# # Function to add a company with English details
# def add_company_en():
#     internal_name = fake.company()
#     # email = fake.email()
#     # companyweb = fake.url()[:20]
#     facebook_page = fake.url()
#     topCompany = random.choice([True, False])
#     visibility = random.choice([True, False])

#     company_en = Company_EN.objects.get_or_create(
#         internal_name=internal_name,
#         # email=email,
#         # companyweb=companyweb,
#         facebook_page=facebook_page,
#         topCompany=topCompany,
#         visibility=visibility
#     )[0]
#     company_en.save()

# # Function to add a company with Georgian details
# def add_company_ka():
#     internal_name = fake.company()[:20]
#     # companyweb = fake.url()[:20]
#     facebook_page = fake.url()[:20]
#     topCompany = random.choice([True, False])
#     visibility = random.choice([True, False])

#     company_ka = Company_KA.objects.get_or_create(
#         internal_name=internal_name,
#         # companyweb=companyweb,
#         facebook_page=facebook_page,
#         topCompany=topCompany,
#         visibility=visibility
#     )[0]
#     company_ka.save()

# # Function to add a company with Russian details
# def add_company_ru():
#     internal_name = fake.company()[:20]
#     # companyweb = fake.url()[:20]
#     facebook_page = fake.url()[:20]
#     topCompany = random.choice([True, False])
#     visibility = random.choice([True, False])

#     company_ru = Company_RU.objects.get_or_create(
#         internal_name=internal_name,
#         # companyweb=companyweb,
#         facebook_page=facebook_page,
#         topCompany=topCompany,
#         visibility=visibility
#     )[0]
#     company_ru.save()


def add_complex_names():
    created_at = timezone.make_aware(fake.date_time_this_decade(), timezone.get_default_timezone())
    internal_complex_name = fake.company_suffix()[:255]
    full_price = Decimal(round(random.uniform(100000, 999999.99), 2))
    price_per_sq_meter = Decimal(round(random.uniform(500, 9999.99), 2))
    finish_year = random.randint(2020, 2030)
    finish_month = random.randint(1, 12)
    status = random.choice([1, 2, 3])
    visibiliti = random.choice([True, False])
    vipComplex = random.choice([True, False])
    floor_number = random.randint(1, 100)
    space = Decimal(round(random.uniform(50, 2000), 2))
    number_of_houses = random.randint(1, 10)
    number_of_floors = random.randint(1, 50)
    phone_number = fake.phone_number()[:20] 
    number_of_apartments = random.randint(10, 500)
    number_of_buildings = random.randint(1, 10)
    flooring = random.randint(1, 5)
    parking_quantity = random.randint(10, 200)
    rooms_quantity = random.randint(1, 10)
    light_percentage = random.randint(0, 100)
    humidity_percentage = random.randint(0, 100)
    area_squareness = Decimal(round(random.uniform(50, 500), 2))
    ceiling_height_meters = Decimal(round(random.uniform(2.5, 5), 2))
    plot_area = Decimal(round(random.uniform(200, 10000), 2))
    rank = random.choice(['A', 'B', 'C', 'D', 'E'])
    
    complex_name = Complex_Names.objects.get_or_create(
        created_at=created_at,
        internal_complex_name=internal_complex_name,
        full_price=full_price,
        price_per_sq_meter=price_per_sq_meter,
        finish_year=finish_year,
        finish_month=finish_month,
        status=status,
        visibiliti=visibiliti,
        vipComplex=vipComplex,
        floor_number=floor_number,
        space=space,
        number_of_houses=number_of_houses,
        number_of_floors=number_of_floors,
        phone_number=phone_number,
        number_of_apartments=number_of_apartments,
        number_of_buildings=number_of_buildings,
        flooring=flooring,
        parking_quantity=parking_quantity,
        rooms_quantity=rooms_quantity,
        light_percentage=light_percentage,
        humidity_percentage=humidity_percentage,
        area_squareness=area_squareness,
        ceiling_height_meters=ceiling_height_meters,
        plot_area=plot_area,
        rank=rank
    )[0]
    complex_name.save()

#Function to add a complex with English details
def add_complex_en():
    created_at = timezone.make_aware(fake.date_time_this_decade(), timezone.get_default_timezone())
    internal_complex_name = fake.company_suffix()[:255]
    full_price = Decimal(round(random.uniform(100000, 999999.99), 2))
    price_per_sq_meter = Decimal(round(random.uniform(500, 9999.99), 2))
    finish_year = random.randint(2020, 2030)
    finish_month = random.randint(1, 12)
    status = random.choice([1, 2, 3])
    visibiliti = random.choice([True, False])
    vipComplex = random.choice([True, False])
    floor_number = random.randint(1, 100)
    space = Decimal(round(random.uniform(50, 2000), 2))
    number_of_houses = random.randint(1, 10)
    number_of_floors = random.randint(1, 50)
    phone_number = fake.phone_number()[:20] 
    number_of_apartments = random.randint(10, 500)
    number_of_buildings = random.randint(1, 10)
    flooring = random.randint(1, 5)
    parking_quantity = random.randint(10, 200)
    rooms_quantity = random.randint(1, 10)
    light_percentage = random.randint(0, 100)
    humidity_percentage = random.randint(0, 100)
    area_squareness = Decimal(round(random.uniform(50, 500), 2))
    ceiling_height_meters = Decimal(round(random.uniform(2.5, 5), 2))
    plot_area = Decimal(round(random.uniform(200, 10000), 2))
    rank = random.choice(['A', 'B', 'C', 'D', 'E'])
    
    complex_en = Complex_EN.objects.get_or_create(
        created_at=created_at,
        internal_complex_name=internal_complex_name,
        full_price=full_price,
        price_per_sq_meter=price_per_sq_meter,
        finish_year=finish_year,
        finish_month=finish_month,
        status=status,
        visibiliti=visibiliti,
        vipComplex=vipComplex,
        floor_number=floor_number,
        space=space,
        number_of_houses=number_of_houses,
        number_of_floors=number_of_floors,
        phone_number=phone_number,
        number_of_apartments=number_of_apartments,
        number_of_buildings=number_of_buildings,
        flooring=flooring,
        parking_quantity=parking_quantity,
        rooms_quantity=rooms_quantity,
        light_percentage=light_percentage,
        humidity_percentage=humidity_percentage,
        area_squareness=area_squareness,
        ceiling_height_meters=ceiling_height_meters,
        plot_area=plot_area,
        rank=rank
    )[0]
    complex_en.save()

# Function to add a complex with Georgian details
def add_complex_ka():
    created_at = timezone.make_aware(fake.date_time_this_decade(), timezone.get_default_timezone())
    internal_complex_name = fake.company_suffix()[:255]
    full_price = Decimal(round(random.uniform(100000, 999999.99), 2))
    price_per_sq_meter = Decimal(round(random.uniform(500, 9999.99), 2))
    finish_year = random.randint(2020, 2030)
    finish_month = random.randint(1, 12)
    status = random.choice([1, 2, 3])
    visibiliti = random.choice([True, False])
    vipComplex = random.choice([True, False])
    floor_number = random.randint(1, 100)
    space = Decimal(round(random.uniform(50, 2000), 2))
    number_of_houses = random.randint(1, 10)
    number_of_floors = random.randint(1, 50)
    phone_number = fake.phone_number()[:20] 
    number_of_apartments = random.randint(10, 500)
    number_of_buildings = random.randint(1, 10)
    flooring = random.randint(1, 5)
    parking_quantity = random.randint(10, 200)
    rooms_quantity = random.randint(1, 10)
    light_percentage = random.randint(0, 100)
    humidity_percentage = random.randint(0, 100)
    area_squareness = Decimal(round(random.uniform(50, 500), 2))
    ceiling_height_meters = Decimal(round(random.uniform(2.5, 5), 2))
    plot_area = Decimal(round(random.uniform(200, 10000), 2))
    rank = random.choice(['A', 'B', 'C', 'D', 'E'])
    
    complex_en = Complex_EN.objects.get_or_create(
        created_at=created_at,
        internal_complex_name=internal_complex_name,
        full_price=full_price,
        price_per_sq_meter=price_per_sq_meter,
        finish_year=finish_year,
        finish_month=finish_month,
        status=status,
        visibiliti=visibiliti,
        vipComplex=vipComplex,
        floor_number=floor_number,
        space=space,
        number_of_houses=number_of_houses,
        number_of_floors=number_of_floors,
        phone_number=phone_number,
        number_of_apartments=number_of_apartments,
        number_of_buildings=number_of_buildings,
        flooring=flooring,
        parking_quantity=parking_quantity,
        rooms_quantity=rooms_quantity,
        light_percentage=light_percentage,
        humidity_percentage=humidity_percentage,
        area_squareness=area_squareness,
        ceiling_height_meters=ceiling_height_meters,
        plot_area=plot_area,
        rank=rank
    )[0]
    complex_en.save()

# Function to add a complex with Russian details
def add_complex_ru():
    created_at = timezone.make_aware(fake.date_time_this_decade(), timezone.get_default_timezone())
    internal_complex_name = fake.company_suffix()[:255]
    full_price = Decimal(round(random.uniform(100000, 999999.99), 2))
    price_per_sq_meter = Decimal(round(random.uniform(500, 9999.99), 2))
    finish_year = random.randint(2020, 2030)
    finish_month = random.randint(1, 12)
    status = random.choice([1, 2, 3])
    visibiliti = random.choice([True, False])
    vipComplex = random.choice([True, False])
    floor_number = random.randint(1, 100)
    space = Decimal(round(random.uniform(50, 2000), 2))
    number_of_houses = random.randint(1, 10)
    number_of_floors = random.randint(1, 50)
    phone_number = fake.phone_number()[:20] 
    number_of_apartments = random.randint(10, 500)
    number_of_buildings = random.randint(1, 10)
    flooring = random.randint(1, 5)
    parking_quantity = random.randint(10, 200)
    rooms_quantity = random.randint(1, 10)
    light_percentage = random.randint(0, 100)
    humidity_percentage = random.randint(0, 100)
    area_squareness = Decimal(round(random.uniform(50, 500), 2))
    ceiling_height_meters = Decimal(round(random.uniform(2.5, 5), 2))
    plot_area = Decimal(round(random.uniform(200, 10000), 2))
    rank = random.choice(['A', 'B', 'C', 'D', 'E'])
    
    complex_en = Complex_EN.objects.get_or_create(
        created_at=created_at,
        internal_complex_name=internal_complex_name,
        full_price=full_price,
        price_per_sq_meter=price_per_sq_meter,
        finish_year=finish_year,
        finish_month=finish_month,
        status=status,
        visibiliti=visibiliti,
        vipComplex=vipComplex,
        floor_number=floor_number,
        space=space,
        number_of_houses=number_of_houses,
        number_of_floors=number_of_floors,
        phone_number=phone_number,
        number_of_apartments=number_of_apartments,
        number_of_buildings=number_of_buildings,
        flooring=flooring,
        parking_quantity=parking_quantity,
        rooms_quantity=rooms_quantity,
        light_percentage=light_percentage,
        humidity_percentage=humidity_percentage,
        area_squareness=area_squareness,
        ceiling_height_meters=ceiling_height_meters,
        plot_area=plot_area,
        rank=rank
    )[0]
    complex_en.save()


def add_ground_names():
    internal_ground_name = fake.word()[:50]
    area = Decimal(round(random.uniform(50, 999999.99), 2))
    price = Decimal(round(random.uniform(10000, 999999.99), 2))
    is_available = random.choice([True, False])
    visibiliti = random.choice([True, False])
    
    ground = Ground_Names.objects.get_or_create(
        internal_ground_name=internal_ground_name,
        area=area,
        price=price,
        is_available=is_available,
        visibiliti=visibiliti
    )[0]
    ground.save()

def add_private_appartment_names():
    created_at = timezone.make_aware(fake.date_time_this_decade(), timezone.get_default_timezone())
    internal_private_apartment_name = fake.word()[:50]
    number_of_rooms = random.choice(['studio', '1', '2', '3', '4', '5+'])
    status = random.choice(['1', '2', '3'])
    area = Decimal(round(random.uniform(20, 99999.99), 2))
    full_price = Decimal(round(random.uniform(10000, 99999.99), 2))
    square_price = Decimal(full_price / area).quantize(Decimal('.01')) if area > 0 else Decimal(0)
    floor_number = random.randint(1, 50)
    is_available = random.choice([True, False])
    visibiliti = random.choice([True, False])
    
    private_appartment = Private_Appartment_Names.objects.get_or_create(
        created_at=created_at, 
        internal_private_apartment_name=internal_private_apartment_name, 
        number_of_rooms=number_of_rooms,
        status=status, 
        area=area,
        full_price=full_price,
        square_price=square_price,
        floor_number=floor_number,
        is_available=is_available,
        visibiliti=visibiliti
    )[0]
    private_appartment.save()

def add_promotions_and_offers_names():
    internal_promotion_name = fake.catch_phrase()[:255]
    start_date = fake.date_between(start_date="-1y", end_date="today")
    end_date = fake.date_between(start_date="today", end_date="+1y")
    discount = Decimal(round(random.uniform(0.01, 999.99), 2)) if random.choice([True, False]) else None
    gift = fake.sentence() if random.choice([True, False]) else None
    installment = random.choice([True, False])
    visibility = random.choice([True, False])
    
    company = random.choice(Company_Names.objects.all()) if Company_Names.objects.exists() else None
    
    promotion = Promotions_and_offers_Names.objects.get_or_create(
        internal_promotion_name=internal_promotion_name, 
        start_date=start_date, 
        end_date=end_date,
        discount=discount, 
        gift=gift,
        installment=installment,
        visibility=visibility,
        company=company  # Make sure you handle the case when no company exists
    )[0]
    promotion.save()

def populate(N=1):
    for _ in range(N):
        add_address_en()
        add_address_ka()
        add_address_ru()

        add_appartment_names()
        
        add_company_names()
        # add_company_en()
        # add_company_ka()
        # add_company_ru()
        
        add_complex_names()
        add_complex_en()
        add_complex_ka()
        add_complex_ru()
        
        add_ground_names()
        add_private_appartment_names()
        add_promotions_and_offers_names()

if __name__ == '__main__':
    print("Populating the databases...Please Wait"  )
    populate()  # You can change the number of samples to generate as needed
    print('Populating Complete')
