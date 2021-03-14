import requests
import os
class DataManager:
    def __init__(self):
        self.destData = {}
    def getDestData(self):
        self.SHEETY_AUTH = os.environ.get("SHEETY_API_KEY")
        self.sheetyEndpoint = f"https://api.sheety.co/{self.SHEETY_AUTH}/flightDeals/prices"

        response = requests.get(url=self.sheetyEndpoint, auth=("AUTH NAME", self.SHEETY_AUTH))

        data = response.json()
        self.destData  = data["prices"]
        return self.destData
    def update(self,sheetData):
        self.sheetData = sheetData
        for self.i in self.sheetData:
            self.id = self.i["id"]
            self.putUrl = f"{self.sheetyEndpoint}/{self.id}"
            self.parameters = {
                "price":{
                    "iataCode":self.i["iataCode"]
                }
            }
            response = requests.put(url=self.putUrl,json=self.parameters,auth=("AUTH NAME", self.SHEETY_AUTH))
