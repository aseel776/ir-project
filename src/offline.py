import requests
import endpoints

baseUrl = 'http://localhost:8000'

# ------------------- PreProcessing 1st Dataset -------------------

output_dir = 'res/ds1'

request_body = {
    'dataset_id': 1,
    'output_dir': output_dir,
}

response = requests.post(f'{baseUrl}{endpoints.PRE_PROCESSING}', json= request_body)

if response.status_code == 200:
    print('1st Dataset Processed Successfully')

    # ------------ Indexing ------------

    data = response.json()
    structured_corpus = data.get('structured_corpus')

    request_body = {
        'corpus': structured_corpus,
        'output_dir': output_dir,
    }

    response = requests.post(f'{baseUrl}{endpoints.INDEXING}', json= request_body)

    print(response.status_code)

else:
    print('Failure in Processing 1st Dataset')

# ------------------- PreProcessing 2nd Dataset -------------------

output_dir = 'res/ds2'

request_body = {
    'dataset_id': 2,
    'output_dir': output_dir,
}

response = requests.post(f'{baseUrl}{endpoints.PRE_PROCESSING}', json= request_body)

if response.status_code == 200:
    print('2nd Dataset Processed Successfully')

    # ------------ Indexing ------------

    data = response.json()
    structured_corpus = data.get('structured_corpus')

    request_body = {
        'corpus': structured_corpus,
        'output_dir': output_dir,
    }

    response = requests.post(f'{baseUrl}{endpoints.INDEXING}', json= request_body)

    print(response.status_code)
else:
    print('Failure in Processing 2nd Dataset')