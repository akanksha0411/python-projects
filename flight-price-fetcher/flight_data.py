class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, dest_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.dest_airport = dest_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("None", "None", "None", "None", "None", "None")
    # Looking for "best_flights" in data, return [] (an empty list if no such Key is found)
    total_flights = data.get("best_flights", []) + data.get("other_flights", [])

    first_flight = total_flights[0]
    lowest_price = first_flight["price"]
    origin_airport = first_flight['flights'][0]['departure_airport']['id']
    destination_airport = first_flight['flights'][-1]['arrival_airport']['id']
    departure_date = first_flight['flights'][0]['departure_airport']['time'].split(" ")[0]

    nr_stops = len(first_flight['flights']) - 1

    cheapest_flight = FlightData(price=lowest_price,
                                 origin_airport=origin_airport,
                                 dest_airport=destination_airport,
                                 out_date=departure_date,
                                 return_date=return_date,
                                 stops=nr_stops)

    for flight in total_flights:
        try:
            price = flight["price"]
        except KeyError:
            print("Price not available")
            continue
        if price < lowest_price:
            lowest_price = price
            origin_airport = flight['flights'][0]['departure_airport']['id']
            destination_airport = flight['flights'][-1]['arrival_airport']['id']
            departure_date = flight['flights'][0]['departure_airport']['time'].split(" ")[0]
            cheapest_flight = FlightData(price=lowest_price,
                                         origin_airport=origin_airport,
                                         dest_airport=destination_airport,
                                         out_date=departure_date,
                                         return_date=return_date,
                                         stops=nr_stops)
            print(f"Lowest price is -> {lowest_price}")

    return cheapest_flight

