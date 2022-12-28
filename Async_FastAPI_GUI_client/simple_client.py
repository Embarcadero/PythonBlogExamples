import requests

BASE = "http://127.0.0.1:8000/"
endpointURL = BASE + "employees"

# GET
response = requests.get(endpointURL)
response = response.json()
print(response)

# POST
params = {"firstName": "Fifa", 
          "lastName": "Badar", 
          "gender": "F", 
          "role": "Teacher", 
          "joinYear":"2022" }
response = requests.post(endpointURL, params=params)
response = response.json()
print(response)
