import os
from delphifmx import *

# Additional Imports
import requests

class MainForm(Form):

    def __init__(self, owner):
        self.TabControl1 = None
        self.HistoricalTab = None
        self.HistoryButton = None
        self.Calendar1 = None
        self.CurrentTab = None
        self.CurrentButton = None
        self.Image1 = None
        self.PredictionTab = None
        self.Edit2 = None
        self.PredictButton = None
        self.TitleLabel = None
        self.CityLabel = None
        self.HistoricalMemo = None
        self.DateLabel = None
        self.CurrentMemo = None
        self.SpinBox1 = None
        self.PredictLabel = None
        self.PredictLabel2 = None
        self.PredictMemo = None
        self.CityCombo = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        # Get all cities in a particular country
        url = "https://api.apilayer.com/geo/country/cities/US"

        payload = {}
        headers= {
        "apikey": "your_api_key"
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        result = response.json()

        # Store all cities in a list and even populate the combo box
        self.cities = []
        for city in result:
            self.CityCombo.Items.Add(city["name"])
            self.cities.append(city["name"])

    def HistoryButtonClick(self, Sender):
        date = '{}-{}-{}'.format(self.Calendar1.DateTime[0], str(self.Calendar1.DateTime[1]).zfill(2), str(self.Calendar1.DateTime[2]).zfill(2)) # Storing date from calendar in the required format
        
        params = {
        'access_key': 'your_api_access_key',
        'query': self.cities[self.CityCombo.ItemIndex],
        'historical_date': date
        }
        
        api_result = requests.get('http://api.weatherstack.com/historical', params)
        api_response = api_result.json()

        self.HistoricalMemo.Lines.Add("Location : " + api_response["location"]["name"])
        self.HistoricalMemo.Lines.Add("Min Temperature : " + str(api_response["historical"][date]["mintemp"]))
        self.HistoricalMemo.Lines.Add("Max Temperature : " + str(api_response["historical"][date]["maxtemp"]))
        self.HistoricalMemo.Lines.Add("Avg Temperature : " + str(api_response["historical"][date]["avgtemp"]))
        self.HistoricalMemo.Lines.Add("UV_Index : " + str(api_response["historical"][date]["uv_index"]))

    def CurrentButtonClick(self, Sender):
        params = {
        'access_key': 'your_api_access_key',
        'query': self.cities[self.CityCombo.ItemIndex]
        }
        
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()

        self.CurrentMemo.Lines.Add("Location : " + api_response["location"]["name"])
        self.CurrentMemo.Lines.Add("Temperature: " + str(api_response["current"]["temperature"]))
        self.CurrentMemo.Lines.Add("Feels Like: " + str(api_response["current"]["feelslike"]))
        self.CurrentMemo.Lines.Add("Description: " + api_response["current"]["weather_descriptions"][0])
        self.CurrentMemo.Lines.Add("Percipitation : " + str(api_response["current"]["precip"]))
        self.CurrentMemo.Lines.Add("Humidity: " + str(api_response["current"]["humidity"]))
        self.CurrentMemo.Lines.Add("Windspeed: " + str(api_response["current"]["wind_speed"]))
        self.CurrentMemo.Lines.Add("Pressure: " + str(api_response["current"]["pressure"]))
        self.CurrentMemo.Lines.Add("UV_Index: " + str(api_response["current"]["uv_index"]))
        self.CurrentMemo.Lines.Add("Visibility: " + str(api_response["current"]["visibility"]))

        # URL of the image you want to load
        image_url = api_response["current"]["weather_icons"][0]

        # Send a GET request to the URL to retrieve the image data
        response = requests.get(image_url)

        if response.status_code == 200:
            # Read the image data from the response content
            image_data = response.content

            # Local path to save the image
            local_path = "image.png"        
            # Save the image locally
            with open(local_path, "wb") as image_file:
                image_file.write(image_data)
            
            self.Image1.Bitmap.LoadFromFile(local_path)

    def PredictButtonClick(self, Sender):
        params = {
        'access_key': 'your_api_access_key',
        'query': self.cities[self.CityCombo.ItemIndex],
        'forecast_days': self.SpinBox1.Text,
        }
        
        api_result = requests.get('http://api.weatherstack.com/forecast', params)
        api_response = api_result.json()

        forecast = api_response["forecast"]

        # Iterate through the forecast dates
        for date, date_data in forecast.items():
            self.PredictMemo.Lines.Add("Date: " + date)
            self.PredictMemo.Lines.Add("Min Temperature: " + str(date_data["mintemp"]))
            self.PredictMemo.Lines.Add("Max Temperature: " + str(date_data["maxtemp"]))
            self.PredictMemo.Lines.Add("Avg Temperature: " + str(date_data["avgtemp"]))
            self.PredictMemo.Lines.Add("UV_Index: " + str(date_data["uv_index"]))
            self.PredictMemo.Lines.Add("")  # Add an empty line for separation