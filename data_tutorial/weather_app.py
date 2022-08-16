import requests
import  json


api_key = "87f7576a97fd4907d06f67ef8c70212f"
user_latitude = input("Enter the latitude: ")
user_longitude = input("Enter the longitude: ")
api = "https://api.openweathermap.org/data/2.5/weather?lat="+(user_latitude)+"&lon="+(user_longitude)+"&appid="+(api_key)

# print (api)

response = requests.get(api)
data = json.loads(response.text)
print (data)

