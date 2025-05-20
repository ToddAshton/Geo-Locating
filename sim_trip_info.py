import requests
import os

def get_trip_info():
    api_key = os.getenv("RAPIDAPI_KEY")
    if not api_key:
        raise Exception("Missing RAPIDAPI_KEY environment variable")

    url = "https://sim-based-location-tracking1.p.rapidapi.com/api/v3/trip/info/"
    headers = {
        "x-rapidapi-host": "sim-based-location-tracking1.p.rapidapi.com",
        "x-rapidapi-key": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("Trip Info:", data)
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Exception:", str(e))

if __name__ == "__main__":
    get_trip_info()
