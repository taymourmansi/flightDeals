import requests
import datetime
from flight_data import FlightData
import os

class FlightSearch:
    def getCityCode(self,city):
        self.endpoint = "https://tequila-api.kiwi.com/locations/query?"
        self.city = city
        self.AUTH = os.environ.get("TEQUILA_AUTH_KEY")
        self.headers = {
            "apikey": self.AUTH,
        }
        self.params = {
            "term":self.city,
        }
        response = requests.get(url=self.endpoint,params=self.params,headers=self.headers)
        self.iata = response.json()["locations"][0]["code"]
        return self.iata



    def searchFlight(self,fromCity,toCity,dateFrom,dateTo):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search?"
        self.AUTH = os.environ.get("TEQUILA_AUTH_KEY")
        self.headers = {
            "apikey": self.AUTH,
        }
        self.params = {
            "fly_from":fromCity,
            "fly_to": toCity,
            "date_from":dateFrom,
            "date_from": dateTo,
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr":"USD",
        }
        response = requests.get(url=self.endpoint, params=self.params, headers=self.headers)
        data = response.json()["data"][0]
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data