import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("SERP_API_KEY")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        query_params = {
            "engine" : "google_flights",
            "departure_id" : origin_city_code,
            "arrival_id" : destination_city_code,
            "outbound_date" : from_time.strftime("%Y-%m-%d"),
            "return_date" : to_time.strftime("%Y-%m-%d"),
            "type" : "1",
            "currency" : "INR",
            "api_key" : self._api_key,
        }
        if is_direct:
            query_params['stops'] = "1"

        response = requests.get(url=str(os.getenv("SERPAPI_ENDPOINT")), params=query_params)

        if response.status_code != 200:
            print(f"check_flights() response code {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error {data['error']}")
            return None
        return data
