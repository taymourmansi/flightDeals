# Flight Deals Alert

The purpose of this application is to help the you find the best and cheapest flights that meet the users price range! Just connect a Google Sheets with the name of your cities and the maximum price you'd like to pay for it. Then all you have to do is wait for the program to find the best deals and you should receive that text message with all the best flights to your destinations.  

## How It Works

The application is using multiple APIs,Sheety,Tequila, and Twilio. It first utilizes Sheety to grab the data from the Google Sheets sheet. Once the data is gathered, we then use the Tequila API to get the IATA code for that city and fills up the IATA column in your Google Sheet. After finishing the data filling, the application uses all this data to search for flights in the next 6 months for a minimum of 4 days and up to 2 weeks that is less than or equal to the price given. It checks for all the destinations given whenever it is running. Once a flight has been found, we use the Twilio API to send you a message with the flight details and a link to the flight.
## How To Run It

In order to run this application, make sure that Python3 is installed on your computer. Once installed, download the entire flightDeals folder. To start make sure you have a Google Sheets sheet with a column for the City, IATA, and Price, and make sure to fill up the City and Price columns with your own data. Once filled up, make sure to edit the notification.py file to include the user's phone number and the sender phone number, as well as the Twilio Key. Lastly, make sure to upload the entire folder up on Python Anywhere and have it run once a day in order for it to try and detect for flights daily.
