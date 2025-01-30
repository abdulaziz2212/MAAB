import requests
from datetime import datetime


#function to search current temperatory of a given city
def temp_search(city):
    
    api_key='b9a180f0ff7ec936a73f5c84dc54be33'   #api_key
    base_url ='https://api.openweathermap.org/data/2.5/weather'   #base_url to request
    
    #parameters of the request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url,params=params)

    if response.status_code == 200:
        data=response.json()
        timestamp = data["dt"]  # Extract Unix timestamp
        current_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')        
        print(f"\n{'City':<15}{'Temperature (°C)':<15} {'Description':<15}{'Time (UTC)'}")
        print("-"*50)      
        print(f"{city.upper():<15} {data['main']['temp']:<15} {data['weather'][0]['description']:<15}{current_time}")
    else:
        print('Error: ', response.json())

city=input('Enter name of the city: \n')
temp_search(city)