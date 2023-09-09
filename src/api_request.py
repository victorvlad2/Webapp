import requests

url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2020","team":"33"}

headers = {
	"X-RapidAPI-Key": "2735a11d4fmsh2567ef89483ead0p197923jsn09bf45131248",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())