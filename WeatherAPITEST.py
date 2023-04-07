import requests

def main():
	user_input = str(input("Enter CITY :"))

	url = "http://api.weatherapi.com/v1/current.json"
	querystring = {"q":f"{user_input}"}

	headers = {
		"Key": " place your key here ",
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	print("RESPONSE STATUS:", response.status_code)

	Country = response.json()["location"]["country"]
	City = response.json()["location"]["name"]
	last_upd = response.json()["current"]["last_updated"]
	Condition = response.json()["current"]["condition"]["text"]
	Temp_c = response.json()["current"]["temp_c"]
	Feels_like_Cels = response.json()["current"]["feelslike_c"]
	Humidity = response.json()["current"]["humidity"]
	wind_in_mph = response.json()["current"]["wind_mph"]
	wind_dir = response.json()["current"]["wind_dir"]

	for i in range(15):
		print()
	print("============================================================OPWEATHER.COM")
	print()
	print(f" *CITY: {City}   *COUNTRY: {Country}")
	print(f" *CONDITION: {Condition}")
	print()
	print(f" - LAST UPDATED {last_upd}")
	print(f" *Temperature: {Temp_c}'C   *Feels like: {Feels_like_Cels}'C")
	print(f" *Humidity: {Humidity}")
	print(f" *Wind: {wind_in_mph} MPH   *Wind Direction: {wind_dir}")
	print()
	print("============================================================OPWEATHER.COM")
	for i in range(11):
		print()
	main()
main()
