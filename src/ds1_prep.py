import requests
import endpoints
import datasets
from utils.loading import load_dict

baseUrl = 'http://localhost:8000'

dataset = datasets.dataset_1
docs = dataset.docs_iter()
corpus = docs
# corpus = list(islice(docs, 10))

# ------------PreProcessing------------

serialized_corpus = []
for doc in corpus:
    entry = {
        'id': doc.doc_id,
        'text': doc.text,
    }
    serialized_corpus.append(entry)
request_body = {
    'corpus': serialized_corpus,
    'directory': 'res/ds1',
}
response = requests.post(f'{baseUrl}{endpoints.PRE_PROCESSING}', json = request_body)
if response.status_code == 200:
    processed_corpus = response.json().get('processed_corpus')
else:
    print(response.status_code)

# ------------Indexing------------

processed_corpus = load_dict('res/ds1/processed_corpus.json')

request_body = {
    'corpus': processed_corpus,
    'directory': 'res/ds1',
}
response = requests.post(f'{baseUrl}{endpoints.INDEXING}', json = request_body)
print(response.status_code)