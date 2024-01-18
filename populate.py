import os
import django
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elitcity.settings")
django.setup()

from complex.models import *

fake = Faker()

# Assuming you already have languages 'en', 'ka', and 'ru' in your Language model
languages = list(Language.objects.all())

# Function to add languages to many-to-many field
def add_languages(instance):
    for lang in random.sample(languages, random.randint(1, len(languages))):
        instance.lang.add(lang)

def genrate_locations(n):
    for _ in range(n):  # Adjust the number of iterations as needed
        # Create cities
        try:
            city_ka = City_KA.objects.create(city_ka=fake.city())
            add_languages(city_ka)

            city_en = City_EN.objects.create(city_en=fake.city())
            add_languages(city_en)

            city_ru = City_RU.objects.create(city_ru=fake.city())
            add_languages(city_ru)
        except django.db.utils.IntegrityError:
                continue     
    for _ in range(n):
        try:
            # Create pharent districts
            city_ka = City_KA.objects.order_by('?').first()
            city_en = City_EN.objects.order_by('?').first()
            city_ru = City_RU.objects.order_by('?').first()

            PharentDistrict_KA.objects.create(city_ka=city_ka, pharentDistrict_ka=fake.city_suffix())
            PharentDistrict_EN.objects.create(city_en=city_en, pharentDistrict_en=fake.city_suffix())
            PharentDistrict_RU.objects.create(city_ru=city_ru, pharentDistrict_ru=fake.city_suffix())

        except django.db.utils.IntegrityError:
            continue
    for _ in range(n):
        try:
            pharentDistrict_ka = PharentDistrict_KA.objects.order_by("?").first()
            pharentDistrict_en = PharentDistrict_EN.objects.order_by("?").first()
            pharentDistrict_ru = PharentDistrict_RU.objects.order_by("?").first()

            District_KA.objects.create(city_ka=city_ka , pharentDistrict_ka=pharentDistrict_ka , district_ka=fake.city_suffix())
            District_EN.objects.create(city_en=city_en , pharentDistrict_en=pharentDistrict_en , district_en=fake.city_suffix())
            District_RU.objects.create(city_ru=city_ru , pharentDistrict_ru=pharentDistrict_ru , district_ru=fake.city_suffix())

        except django.db.utils.IntegrityError:
            continue

    for _ in range(n):
        try:
            district_ka = District_KA.objects.order_by("?").first()
            district_en = District_EN.objects.order_by("?").first()
            district_ru = District_RU.objects.order_by("?").first()

            Street_Name_KA.objects.create(city_ka=city_ka, pharentDistrict_ka=pharentDistrict_ka, district_ka=district_ka, street_name_ka=fake.city_suffix())
            Street_Name_EN.objects.create(city_en=city_en, pharentDistrict_en=pharentDistrict_en, district_en=district_en, street_name_en=fake.city_suffix())
            Street_Name_RU.objects.create(city_ru=city_ru, pharentDistrict_ru=pharentDistrict_ru, district_ru=district_ru, street_name_ru=fake.city_suffix())

        except django.db.utils.IntegrityError:
            continue

    for _ in range(n):
        try:
            street_name_ka = Street_Name_KA.objects.order_by("?").first()
            street_name_en = Street_Name_EN.objects.order_by("?").first()
            street_name_ru = Street_Name_RU.objects.order_by("?").first()

            Address_KA.objects.create(city_ka=city_ka, pharentDistrict_ka=pharentDistrict_ka, district_ka=district_ka, street_name_ka=street_name_ka, address_ka=fake.address()[:30], longitude=fake.longitude(), latitude=fake.latitude())
            Address_EN.objects.create(city_en=city_en, pharentDistrict_en=pharentDistrict_en, district_en=district_en, street_name_en=street_name_en, address_en=fake.address()[:30], longitude=fake.longitude(), latitude=fake.latitude())
            Address_RU.objects.create(city_ru=city_ru, pharentDistrict_ru=pharentDistrict_ru, district_ru=district_ru, street_name_ru=street_name_ru, address_ru=fake.address()[:30], longitude=fake.longitude(), latitude=fake.latitude())


        except django.db.utils.IntegrityError:
            continue




def create_fake_company():
    # Create a company name entry
    company_name = Company_Names.objects.create(
        internal_name=fake.company(),
        Mobile=fake.phone_number()[:20],
        Mobile_Home=fake.phone_number()[:20],
        email=fake.email(),
        companyweb=fake.url(),
        facebook_page=fake.url(),
        topCompany=random.choice([True, False]),
        visibility=random.choice([True, False])
    )

    # Create a company images entry
    company_images = Company_Images.objects.create(
        internal_name=company_name,
        logocompany=fake.image_url(),
        background_image=fake.image_url()
    )

    # Create localized company entries
    Company_KA.objects.create(
        internal_name=company_images,
        name_ka=company_name.internal_name,
        address_ka=fake.address(),
        aboutcompany_ka=fake.text()
    )

    Company_EN.objects.create(
        internal_name=company_images,
        name_en=company_name.internal_name,
        address_en=fake.address(),
        aboutcompany_en=fake.text()
    )

    Company_RU.objects.create(
        internal_name=company_images,
        name_ru=company_name.internal_name,
        address_ru=fake.address(),
        aboutcompany_ru=fake.text()
    )

def generate_companies(n):
    for _ in range(n):
        create_fake_company()
# ------------------------------------------------------------------------------------------------------------
import time

# nique_name = f"{fake.word()}_{fake.word()}_{int(time.time())}_{random.randint(1000, 9999)}"

def generate_complexes(n):
    for _ in range(n):
        try:
            price_per_sq_meter = fake.random_int(min=100, max=10000)
            unique_name = f"{fake.word()}_{random.randint(1000, 9999)}_{int(time.time())}"
            unique_suffix = f"{int(time.time())}-{random.randint(1000, 9999)}"

            complex_name = Complex_Names.objects.create(
                internal_complex_name=unique_name,
                full_price=random.uniform(100000, 1000000),
                price_per_sq_meter=price_per_sq_meter,  # Assign the random value
                finish_year=random.randint(2020, 2030),
                finish_month=random.randint(1, 12),
                status=random.choice([1, 2, 3]),
                visibiliti=random.choice([True, False]),
                vipComplex=random.choice([True, False]),
                floor_number=random.randint(1, 50),
                space=random.uniform(1000, 5000),
                number_of_apartments=random.randint(1, 100),
                number_of_houses=random.randint(1, 50),
                number_of_floors=random.randint(1, 10),
                complex_level=random.randint(1, 5),
                phone_number=fake.phone_number()[:20],
                plot_area=random.uniform(500, 10000),
                rank=random.choice(['A', 'B', 'C', 'D', 'E'])
            )

            # Now create the corresponding Complex models in all languages
            complex_images = Complex_Images.objects.create(
                internal_complex_name=complex_name,
                images=fake.image_url()
            )


            # Randomly select companies and addresses from those already created
            company_ka = Company_KA.objects.order_by('?').first()
            address_ka = Address_KA.objects.order_by('?').first()

            company_en = Company_EN.objects.order_by('?').first()
            address_en = Address_EN.objects.order_by('?').first()

            company_ru = Company_RU.objects.order_by('?').first()
            address_ru = Address_RU.objects.order_by('?').first()

            if not company_ka or not address_ka:
                continue  # Skip this iteration if company or address is None
            

            if not company_en or not address_en:
                continue

            if not company_ru or not address_ru:
                continue

            # Create localized complex instances
            Complex_KA.objects.create(
                internal_complex_name=complex_name,
                complex_images=complex_images,
                company_ka=company_ka,
                address_ka=address_ka,
                complex_name_ka=f"{fake.company_suffix()}_{unique_suffix}",
                type_of_roof_ka=fake.word()
            )

            Complex_EN.objects.create(
                internal_complex_name=complex_name,
                complex_images=complex_images,
                company_en=company_en,
                address_en=address_en,
                complex_name_en=f"{fake.company_suffix()}_{unique_suffix}",
                type_of_roof_en=fake.word()
            )

            Complex_RU.objects.create(
                internal_complex_name=complex_name,
                complex_images=complex_images,
                company_ru=company_ru,
                address_ru=address_ru,
                complex_name_ru=f"{fake.company_suffix()}_{unique_suffix}",
                type_of_roof_ru=fake.word()
            )
        except django.db.utils.IntegrityError as e:
            print(f"Integrity error: {e}")  # Print the error for debugging
            continue


# genrate_locations(60)
# generate_companies(8)
generate_complexes(60)