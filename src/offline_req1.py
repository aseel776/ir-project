import requests
import core.base_urls as urls

# ------------------- PreProcessing 1st Dataset -------------------

output_dir = '../res/ds1'

request_body = {
    'dataset_id': 1,
    'output_dir': output_dir,
}

response = requests.post(urls.PRE_PROCESSING_URL, json= request_body)

if response.status_code == 200:
    print('1st Dataset Processed Successfully')

    # ------------ Indexing ------------

    data = response.json()
    structured_corpus = data.get('structured_corpus')

    request_body = {
        'corpus': structured_corpus,
        'output_dir': output_dir,
    }

    response = requests.post(urls.INDEXING_URL, json= request_body)

    print(response.status_code)

else:
    print('Failure in Processing 1st Dataset')