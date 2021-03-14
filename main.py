from data_manager import DataManager
from flight_search import FlightSearch
import notification_manager
import datetime
dataManager = DataManager()
sheetData = dataManager.getDestData()
for city in sheetData:
    if len(city['iataCode']) < 1:
        flightData = FlightSearch().getCityCode(city["city"])
        city['iataCode'] = flightData
dataManager.update(sheetData)

today = datetime.datetime.today().date()
dateFrom = (today + datetime.timedelta(1)).strftime("%d/%m/%Y")
dateTo = (today + datetime.timedelta(180)).strftime("%d/%m/%Y")

for i in sheetData:
    flightSearch = FlightSearch()
    flight = flightSearch.searchFlight(fromCity="BOS",toCity=i["iataCode"],dateFrom=dateFrom,dateTo=dateTo)
    if flight.price < i["lowestPrice"]:
        notification_manager.sendAlert(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )