import os
import django
from faker import Faker
import random
import glob
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elitcity.settings")
django.setup()

from complex.models import *



fake = Faker()




def get_image_list():
    # Get the full path to the random_images folder
    images_path = os.path.join(os.path.dirname(__file__), 'random_images')
    # Use glob to get all the image files
    image_files = glob.glob(os.path.join(images_path, '*.[jJ][pP][gG]'))
    
    return image_files

# This will give you a list of paths to the images
image_list = get_image_list()
selected_image_path = random.choice(image_list)
selected_image_name = os.path.basename(selected_image_path)





# Assuming you already have languages 'en', 'ka', and 'ru' in your Language model
languages = list(Language.objects.all())

# Function to add languages to many-to-many field
def add_languages(instance):
    for lang in random.sample(languages, random.randint(1, len(languages))):
        instance.lang.add(lang)

def genrate_locations(n):
    for _ in range(1):  # Adjust the number of iterations as needed
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

        
    for _ in range(3):
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






def get_company_image_list():
    images_path = os.path.join(os.path.dirname(__file__), 'random_company_logo')
    # Adjust the glob pattern to search for both .jpg and .png files
    image_files = glob.glob(os.path.join(images_path, '*.[jJ][pP][gG]')) + glob.glob(os.path.join(images_path, '*.[pP][nN][gG]'))
    return image_files

def get_background_image_list():
    images_path = os.path.join(os.path.dirname(__file__), 'random_background_company')
    image_files = glob.glob(os.path.join(images_path, '*.[jJ][pP][gG]'))
    return image_files


def create_fake_company():
    # Create a company name entry 
    company_fake_name = fake.company()
    company_name = Company_Names.objects.create(
        internal_name=company_fake_name,
        Mobile=fake.phone_number()[:20],
        Mobile_Home=fake.phone_number()[:20],
        email=fake.email(),
        companyweb=fake.url(),
        facebook_page=fake.url(),
        topCompany=random.choice([False , True]),
        visibility=random.choice([True])
    )

    # Select a logo image from your predefined images directory for companies
    company_logo_image_path = random.choice(get_company_image_list())
    company_logo_image_name = os.path.basename(company_logo_image_path)

    # Get the full path to the random_background_images folder and select a background image
    background_image_path = random.choice(get_background_image_list())
    background_image_name = os.path.basename(background_image_path)

    # Create corresponding company images
    for _ in range(3): 
        with open(company_logo_image_path, 'rb') as logo_file, open(background_image_path, 'rb') as background_file:
            company_images = Company_Images.objects.create(
                internal_name=company_name,
                logocompany=File(logo_file, name=company_logo_image_name),
                background_image=File(background_file, name=background_image_name)
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

    print(f'Generated company: {company_fake_name}')

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
                number_of_floors=random.randint(1, 10),
                phone_number=fake.phone_number()[:20],
                plot_area=random.uniform(500, 10000),
                rank=random.choice(['A', 'B', 'C', 'D', 'E'])
            )

            for _ in range(7):
                # Now create the corresponding Complex models in all languages
                selected_image_path = random.choice(get_image_list())
                selected_image_name = os.path.basename(selected_image_path)
                with open(selected_image_path, 'rb') as img_file:
                    complex_images = Complex_Images.objects.create(
                        internal_complex_name=complex_name,
                        images=File(img_file, name=selected_image_name)
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

            print(f"Generated ground: {unique_name}")

        except django.db.utils.IntegrityError as e:
            print(f"Integrity error: {e}")  # Print the error for debugging
            continue




def get_apartment_images():
    images_path = os.path.join(os.path.dirname(__file__), 'random_appartment_images')
    image_files = glob.glob(os.path.join(images_path, '*.[jJ][pP][gG]'))
    return image_files



def generate_private_apartments(n):
    for _ in range(n):
        try:
            internal_name = f"{fake.word()}_{random.randint(1000, 9999)}_{int(time.time())}"
            number_of_rooms = random.choice(['studio', '1', '2', '3', '4', '5+'])
            status = random.choice(['1', '2', '3'])
            area = random.uniform(30, 300)
            full_price = random.uniform(50000, 1000000)
            square_price = full_price / area
            floor_number = random.randint(1, 50)
            is_available = random.choice([True, False])
            visibiliti = random.choice([True, False])

            private_apartment = Private_Appartment_Names.objects.create(
                internal_private_apartment_name=internal_name,
                number_of_rooms=number_of_rooms,
                status=status,
                area=area,
                full_price=full_price,
                square_price=square_price,
                floor_number=floor_number,
                is_available=is_available,
                visibiliti=visibiliti
            )


            for _ in range(7):
                selected_image_path = random.choice(get_apartment_images())
                selected_image_name = os.path.basename(selected_image_path)  # Corrected to use selected_image_path
                # Create corresponding apartment images
                with open(selected_image_path, 'rb') as img_file:
                    apartment_images = Private_Appartment_images.objects.create(
                        internal_private_apartment_name=private_apartment,
                        images=File(img_file, name=selected_image_name)
                    )


            # Randomly select addresses from those already created
            address_en = Address_EN.objects.order_by('?').first()
            address_ka = Address_KA.objects.order_by('?').first()
            address_ru = Address_RU.objects.order_by('?').first()

            if not (address_en and address_ka and address_ru):
                continue

            # Create localized private apartment instances
            Private_Appartment_EN.objects.create(
                internal_private_apartment_name=private_apartment,
                private_apartment_images=apartment_images,
                private_apartment_address_en=address_en,
                private_apartment_name_en=f"{fake.company_suffix()}_{internal_name}",
                test_private_field_en=fake.word()
            )

            Private_Appartment_KA.objects.create(
                internal_private_apartment_name=private_apartment,
                private_apartment_images=apartment_images,
                private_apartment_address_ka=address_ka,
                private_apartment_name_ka=f"{fake.company_suffix()}_{internal_name}",
                test_private_field_ka=fake.word()
            )

            Private_Appartment_RU.objects.create(
                internal_private_apartment_name=private_apartment,
                private_apartment_images=apartment_images,
                private_apartment_address_ru=address_ru,
                private_apartment_name_ru=f"{fake.company_suffix()}_{internal_name}",
                test_private_field_ru=fake.word()
            )

            print(f"Generated ground: {internal_name}")

        except django.db.utils.IntegrityError as e:
            print(f"Integrity error: {e}")
            continue


def generate_apartments(n):
    for _ in range(n):
        try:
            internal_name = f"{fake.word()}_{random.randint(1000, 9999)}_{int(time.time())}"
            number_of_rooms = random.choice(['studio', '1', '2', '3', '4', '5+'])
            status = random.choice(['1', '2', '3'])
            area = random.uniform(30, 300)
            full_price = random.uniform(50000, 1000000)
            square_price = full_price / area
            floor_number = random.randint(1, 50)
            is_available = random.choice([True, False])
            visibiliti = random.choice([True, False])

            # Optional boolean fields
            metro = random.choice([True, False])
            pharmacy = random.choice([True, False])
            supermarket = random.choice([True, False])
            square = random.choice([True, False])

            apartment = Appartment_Names.objects.create(
                internal_apartment_name=internal_name,
                number_of_rooms=number_of_rooms,
                status=status,
                area=area,
                full_price=full_price,
                square_price=square_price,
                floor_number=floor_number,
                is_available=is_available,
                visibiliti=visibiliti,
                metro=metro,
                Pharmacy=pharmacy,
                supermarket=supermarket,
                square=square
            )

            for _ in range(7):
                selected_image_path = random.choice(get_apartment_images())
                selected_image_name = os.path.basename(selected_image_path)
                # Create corresponding apartment images
                with open(selected_image_path, 'rb') as img_file:
                    apartment_images = Appartment_Images.objects.create(
                        internal_apartment_name=apartment,
                        images=File(img_file, name=selected_image_name)
                    )


            # Randomly select addresses and complexes from those already created
            address_en = Address_EN.objects.order_by('?').first()
            address_ka = Address_KA.objects.order_by('?').first()
            address_ru = Address_RU.objects.order_by('?').first()
            complex_ka = Complex_KA.objects.order_by('?').first()
            complex_en = Complex_EN.objects.order_by('?').first()
            complex_ru = Complex_RU.objects.order_by('?').first()

            if not (address_en and address_ka and address_ru):
                continue
            
            appartment_name_en = fake.company_suffix()[:25]
            appartment_name_ka = fake.company_suffix()[:25]
            appartment_name_ru = fake.company_suffix()[:25]

            # Create localized apartment instances
            Appartment_EN.objects.create(
                internal_apartment_name=apartment,
                complex_en=complex_en,
                appartment_name_en=appartment_name_en,
                appartment_images=apartment_images,
                appartment_address_en=address_en,
                test_field_en=fake.word()
            )

            Appartment_KA.objects.create(
                internal_apartment_name=apartment,
                complex_ka=complex_ka,
                appartment_name_ka=appartment_name_ka,
                appartment_images=apartment_images,
                appartment_address_ka=address_ka,
                test_field_ka=fake.word()
            )

            Appartment_RU.objects.create(
                internal_apartment_name=apartment,
                complex_ru=complex_ru,
                appartment_name_ru=appartment_name_ru,
                appartment_images=apartment_images,
                appartment_address_ru=address_ru,
                test_field_ru=fake.word()
            )

            print(f"Generated apartment: {internal_name}")

        except django.db.utils.IntegrityError as e:
            print(f"Integrity error: {e}")
            continue



def get_ground_image_list():
    # Get the full path to the random_images folder
    images_path = os.path.join(os.path.dirname(__file__), 'random_ground_images')
    # Use glob to get all the image files
    image_files = glob.glob(os.path.join(images_path, '*.[jJ][pP][gG]'))
    
    return image_files

# This will give you a list of paths to the images
ground_image_list = get_ground_image_list()
ground_selected_image_path = random.choice(ground_image_list)
ground_selected_image_name = os.path.basename(ground_selected_image_path)





def generate_grounds(n):
    for _ in range(n):
        try:
            internal_name = f"{fake.word()}_{random.randint(1000, 9999)}_{int(time.time())}"
            area = random.uniform(500, 10000)
            full_price = random.uniform(100000, 2000000)
            square_price = full_price / area
            is_available = random.choice([True, False])
            visibiliti = random.choice([True, False])
            status = random.choice(["1", "2", "3"])
            rank = random.choice(['A', 'B', 'C', 'D', 'E'])
            about_land = fake.text(max_nb_chars=200)
            ground = Ground_Names.objects.create(
                internal_ground_name=internal_name,
                area=area,
                full_price=full_price,
                square_price=square_price,
                is_available=is_available,
                visibiliti=visibiliti,
                status=status,
                rank=rank,
                about_land = about_land
            )


            for _ in range(7):
                ground_selected_image_path = random.choice(get_ground_image_list())
                ground_selected_image_name = os.path.basename(ground_selected_image_path)
            # Create corresponding ground images
                with open(ground_selected_image_path, 'rb') as img_file:
                    ground_images = Ground_Images.objects.create(
                        internal_ground_name=ground,
                        images=File(img_file, name=ground_selected_image_name)
                    )

            # Randomly select addresses from those already created
            address_en = Address_EN.objects.order_by('?').first()
            address_ka = Address_KA.objects.order_by('?').first()
            address_ru = Address_RU.objects.order_by('?').first()

            if not (address_en and address_ka and address_ru):
                continue

            # Create localized ground instances
            Ground_EN.objects.create(
                internal_ground_name=ground,
                ground_name_en=f"{fake.company_suffix()}_{internal_name}",
                ground_images=ground_images,
                ground_address_en=address_en
            )

            Ground_KA.objects.create(
                internal_ground_name=ground,
                ground_name_ka=f"{fake.company_suffix()}_{internal_name}",
                ground_images=ground_images,
                ground_address_ka=address_ka
            )

            Ground_RU.objects.create(
                internal_ground_name=ground,
                ground_name_ru=f"{fake.company_suffix()}_{internal_name}",
                ground_images=ground_images,
                ground_address_ru=address_ru
            )

            print(f"Generated ground: {internal_name}")

        except django.db.utils.IntegrityError as e:
            print(f"Integrity error: {e}")
            continue




# ------------------------------------------promotions --------------------------------------------

def get_promotion_image_list():
    images_path = os.path.join(os.path.dirname(__file__), 'random_ground_images')
    image_files = glob.glob(os.path.join(images_path, '*.[jJ][pP][gG]'))
    return image_files


def generate_promotions_and_offers(n):
    image_list = get_promotion_image_list()
    
    for _ in range(n):
        company = random.choice(Company_Names.objects.all())
        internal_name = f"Promotion_{fake.word()}_{random.randint(1000, 9999)}"
        start_date = fake.date_between(start_date="-1y", end_date="today")
        end_date = fake.date_between(start_date="today", end_date="+1y")
        
        promotion = Promotions_and_offers_Names.objects.create(
            internal_promotion_name=internal_name,
            start_date=start_date,
            end_date=end_date,
            company=company,
            discount=random.choice([True, False]),
            gift=random.choice([True, False]),
            installment=random.choice([True, False]),
            visibility=random.choice([True, False])
        )

        # Create promotion images
        images = []
        for _ in range(random.randint(2, 5)):  # Generate between 2 to 5 images for each promotion
            selected_image_path = random.choice(image_list)
            selected_image_name = os.path.basename(selected_image_path)
            with open(selected_image_path, 'rb') as img_file:
                image = Promotions_and_offers_Images.objects.create(
                    internal_promotion_name=promotion,
                    images=File(img_file, name=selected_image_name)
                )
                images.append(image)

        # Assuming the first image is used for promotion details in localized models
        first_image = images[0] if images else None

        # Create localized promotion entries
        about_text = fake.text(max_nb_chars=200)  # Sample text for about field
        Promotions_and_offers_KA.objects.create(
            internal_promotion_name=promotion,
            promotion_name_ka=internal_name + " KA",
            promotion_images=first_image,
            alert_ka=about_text,
            about_ka=about_text
        )
        Promotions_and_offers_EN.objects.create(
            internal_promotion_name=promotion,
            promotion_name_en=internal_name + " EN",
            promotion_images=first_image,
            alert_en=about_text,
            about_en=about_text
        )
        Promotions_and_offers_RU.objects.create(
            internal_promotion_name=promotion,
            promotion_name_ru=internal_name + " RU",
            promotion_images=first_image,
            alert_ru=about_text,
            about_ru=about_text
        )

        print(f"Generated promotion: {internal_name} with images and localized details.")







def generate_all_data():
    try:
        print("Generating Locations...")
        genrate_locations(15)
        print("Locations generated.")

        print("Generating Companies...")
        generate_companies(10)
        print("Companies generated.")

        print("Generating Complexes...")
        generate_complexes(15)
        print("Complexes generated.")

        print("Generating Private Apartments...")
        generate_private_apartments(15)
        print("Private Apartments generated.")

        print("Generating Apartments...")
        generate_apartments(15)
        print("Apartments generated.")

        print("Generating Grounds...")
        generate_grounds(15)
        print("Grounds generated.")

        print("Generating promotions...")
        generate_promotions_and_offers(15)
        print("Promotions generated.")

        
        
    except Exception as e:
        print(f"An error occurred: {e}")

generate_all_data()


