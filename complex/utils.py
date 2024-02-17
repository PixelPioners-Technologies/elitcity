# utils.py
import requests
import boto3
from django.conf import settings
AWS_ACCESS_KEY_ID =settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME

def get_nearby_places(latitude, longitude, radius, keyword, api_key):
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{latitude},{longitude}",
        'radius': radius,
        'keyword': keyword,
        'key': api_key
    }

    response = requests.get(endpoint_url, params=params)
    return response.json()  # Return the JSON response from Google Maps API
class S3Helper:
    @staticmethod
    def generate_signed_url(object_key):
            s3 = boto3.client('s3',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            signed_url = s3.generate_presigned_url(ClientMethod ='get_object',
                                                Params={'Bucket': AWS_STORAGE_BUCKET_NAME,
                                                        'Key': object_key},
                                                ExpiresIn=604800)
            return signed_url