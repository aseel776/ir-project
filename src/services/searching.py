import requests
from core.endpoints import SEARCHING
from core.base_urls import QUERY_PROCESSING_URL, MATCHING_URL
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(SEARCHING)
async def start(body: dict = Body()):
    print('New request to searching service !!')
    print(body)

    # get params
    dataset_id = body.get('dataset_id')
    search_text = body.get('search_text')

    # set input dir based on dataset id
    input_dir = f'../res/ds{dataset_id}'

    request_body = {
        'input_dir': input_dir,
        'query': search_text
    }

    # process query
    response = requests.post(QUERY_PROCESSING_URL, json = request_body)

    if response.status_code == 200:
        # get processed query
        data = response.json()
        processed_query = data['processed_query']

        request_body = {
            'input_dir': input_dir,
            'processed_query': processed_query
        }

        # get relevent docs
        response = requests.post(MATCHING_URL, json = request_body)

        if response.status_code == 200:
            return {'data': 'Search completed!'}
        else:
            return {'error': 'Something went wrong during matching!'}

    else:
        return {'error': 'Something went wrong during query processing!'}