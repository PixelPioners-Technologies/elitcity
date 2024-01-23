# utils.py
import requests

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
