from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment
gapi_key = os.getenv('google_apikey')
engine_id = os.getenv('google_engineid')

# Function to fetch an image from Google based on dish name
def fetch_image_from_google(dish_name):
    api_key = gapi_key  
    search_engine_id = engine_id 
    search_url = f"https://www.googleapis.com/customsearch/v1?q={dish_name}&cx={search_engine_id}&key={api_key}&searchType=image"
    
    response = requests.get(search_url)
    
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            # Return the first image result
            return data['items'][0]['link']
    return None