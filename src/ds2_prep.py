import os
import requests
import endpoints
from utils.loading import load_df, load_dict

baseUrl = 'http://localhost:8000'

dataset_path = os.path.join('..', 'Datasets', 'wikIR1k')

# queries_path = os.path.join(dataset_path, 'training', 'queries.csv')
# queries_df = load_df(queries_path)

docs_path = os.path.join(dataset_path, 'documents.csv')
docs_df = load_df(docs_path)


# ------------PreProcessing------------

serialized_corpus = []

for index, row in docs_df.iterrows():
    entry = {
        'id': row['id_right'],
        'text': row['text_right'],
    }
    serialized_corpus.append(entry)

request_body = {
    'corpus': serialized_corpus,
    'directory': 'res/ds2',
}
response = requests.post(f'{baseUrl}{endpoints.PRE_PROCESSING}', json = request_body)
if response.status_code == 200:
    processed_corpus = response.json().get('processed_corpus')
else:
    print(response.status_code)

# ------------Indexing------------

processed_corpus = load_dict('res/ds2/processed_corpus.json')

request_body = {
    'corpus': processed_corpus,
    'directory': 'res/ds2',
}
response = requests.post(f'{baseUrl}{endpoints.INDEXING}', json = request_body)
print(response.status_code)