#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os

import requests_cache
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight, FlightData

requests_cache.install_cache(
    'flight_cache',
    backend='sqlite',
    urls_expire_after= {
    "*.sheety.co*": requests_cache.DO_NOT_CACHE,
    "*": 3600})


data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
# pprint(sheet_data)

# Parameterize the script
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=180)

for data in sheet_data:
    city = data["iataCode"]
    flight_search = FlightSearch()
    print(f"Fetching direct flights for {data['city']} ........ please wait........")
    flights = flight_search.check_flights(
        origin_city_code="DEL",
        destination_city_code=city,
        from_time=tomorrow,
        to_time=six_months_from_today,
        is_direct=True
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{data['city']}: INR {cheapest_flight.price}")

    if cheapest_flight.price == "None":
        print(f"No direct flights found for {data['city']}..... searching for indirect flights for {data['city']}.........")
        stopover_flights = flight_search.check_flights(
            origin_city_code=os.getenv("ORIGIN_CITY_IATA"),
            destination_city_code=city,
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))

    if cheapest_flight.price != "None" and cheapest_flight.price < data['lowestPrice']:
        pprint(f"Lower price flight found to {data['city']}! with {cheapest_flight.stops}")
        data_manager.update_sheet(_id=data['id'], new_price=cheapest_flight.price)
