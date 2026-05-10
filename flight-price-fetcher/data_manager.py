import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_user = os.getenv("SHEETY_USERNAME")
        self.sheety_password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self.sheety_user, self.sheety_password)
        self.destination_data = {}

    def get_sheet_data(self):
        response = requests.get(url=os.getenv("SHEETY_ENDPOINT"), auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_sheet(self, _id, new_price):
        new_data = {
            "price": {
                "serpPrice": new_price,
            }
        }
        response = requests.put(
            url=f"{os.getenv("SHEETY_ENDPOINT")}/{_id}",
            json=new_data,
            auth=self._authorization
        )

        print(response.json())
        print(response.status_code)


