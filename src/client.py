import requests
import endpoints
import ir_datasets

baseUrl = 'http://localhost:8000'

request_data = {
    # 'text': 'Hi! This is a test text. its purpose is to check functions.',
    # 'text': 'test123. test. 245. hi, gi24',
    # 'text': 'Let''s meet for coffee at 2:00 p.m. afterwards we can go for a run!'
    'text': 'let''s go running afterwards. we are happy to join your class'
}
response = requests.post(f"{baseUrl}{endpoints.TEXT_PROCESSING}", json = request_data)