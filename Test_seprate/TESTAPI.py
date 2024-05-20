import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://api.example.com/endpoint'  # Replace 'api.example.com' with the actual hostname
payload = {
    'email': 'ki3@gmail.com',
    'password': 'Artoon1#'
}
auth = HTTPBasicAuth('guest', 'sundanceDev#20')

try:
    response = requests.post(url, json=payload, auth=auth)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

    if response.status_code == 200:
        try:
            data = response.json()
            print(data)
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print('Failed to send data. Status code:', response.status_code)

except requests.exceptions.RequestException as e:
    print("Request error:", e)
