import requests

ngrok_url = 'https://4841-213-230-72-114.ngrok-free.app'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.json()['data'])