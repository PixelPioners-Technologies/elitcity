import os
import django
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elitcity.settings")
django.setup()

from .complex.models import *  # replace 'your_app' with the actual name of your app
from .complex.models import City_KA

faker = Faker()

# Add Languages
languages = ['EN', 'KA', 'RU']
for lang in languages:
    Language.objects.get_or_create(language=lang)

# Get all languages
language_objects = list(Language.objects.all())

def add_languages(m2m_field):
    for _ in range(random.randint(1, len(language_objects))):  # Random number of languages
        m2m_field.add(random.choice(language_objects))

# Generate fake data for City, PharentDistrict, etc.
def generate_fake_data(n):
    for _ in range(n):
        city_ka = City_KA.objects.create(city_ka=faker.city())
        add_languages(city_ka.lang)

        city_en = City_EN.objects.create(city_en=faker.city())
        add_languages(city_en.lang)

        city_ru = City_RU.objects.create(city_ru=faker.city())
        add_languages(city_ru.lang)
        
        # Add more fake data for other models similarly

def generate_fake_datadata(n):
    for _ in range(n):
        # ... existing code to create cities ...

        # Create addresses
        address_ka = Address_KA.objects.create(
            city_ka=City_KA.city_ka,
            address_ka=faker.address(),
            longitude=faker.longitude(),
            latitude=faker.latitude()
        )
        add_languages(address_ka.lang)

        address_en = Address_EN.objects.create(
            city_en=City_EN.city_en,
            address_en=faker.address(),
            longitude=faker.longitude(),
            latitude=faker.latitude()
        )
        add_languages(address_en.lang)

        address_ru = Address_RU.objects.create(
            city_ru=City_RU.city_ru,
            address_ru=faker.address(),
            longitude=faker.longitude(),
            latitude=faker.latitude()
        )
        add_languages(address_ru.lang)
        
        # ... create PharentDistrict, District, Street_Name, etc. ...

# Call the function to create fake data
generate_fake_data(10)  # generates data for 10 c

# Call the function to create fake data
generate_fake_datadata(10)  # generates data for 10 cities, adjust as needed

print("Fake data generation complete.")
