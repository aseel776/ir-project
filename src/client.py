import requests
import endpoints

baseUrl = 'http://localhost:8000'

text = 'Hi from requests.py. This is a test text'
data = {
    'text': text
}

response =  requests.post(url= f"{baseUrl}{endpoints.TEXT_PROCESSING}", json=data)
print(response.json())

