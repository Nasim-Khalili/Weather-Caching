from requests import get
from redis import Redis
from celery_app import app

def get_temperature(city):
    redis_client = Redis(host='localhost', port=6379, db=2, decode_responses=True)
    
    cached_temp = redis_client.get(f'temp:{city}')
    if cached_temp:
        return f"{city}: {cached_temp}°C (cached)"
    
    try:
        
        response = get("https://api.openweathermap.org/data/2.5/weather", 
                       params={"q": city, "appid": "0d23a5d5359bbcc7bba85a273ec6e3e8"})

        data = response.json()
        temp_c = int(data['main']['temp']) - 273 

        redis_client.set(f'temp:{city}', temp_c, ex=60)
        return f"{city}: {temp_c}°C"
    
    except Exception as e:
        return f"{city}: Error - {str(e)}"

@app.task
def fetch_weather_of_cities():
    cities = [
    'Hashtpar',
    'Astara',
    'Eslamshahr',
    'Haviq',
    'Fuman',
    'Bandar-e Anzali',
    'Rasht',
    'Rezvanshahr',
    'SomehSara',
    'Lahijan'
]

    results = [get_temperature(city) for city in cities]
    return results
