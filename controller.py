import requests
from dotenv import load_dotenv
import os



#Load environment variables
load_dotenv()

#Assign environment variables
openweather_id = os.getenv("openweather_id")
openweather_key = os.getenv("openweather_key")

def get_data(place, forecast_days= None):
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={openweather_key}"
    response = requests.get(api_url)
    data = response.json()
    filtered_data = data["list"]
    nb_values = 8 * forecast_days
    filtered_data = filtered_data[:nb_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place= "Tokyo", forecast_days=""))
