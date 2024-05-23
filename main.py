import requests

url = "https://chat-gpt26.p.rapidapi.com/"

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": "Сформувати документ з любої теми"
		}
	]
}
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "6b060f05c7msh53183ba8b89206dp1a7d22jsn6a688890bc9f",
	"X-RapidAPI-Host": "chat-gpt26.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())