import requests
import endpoints
import datasets
from itertools import islice

baseUrl = 'http://localhost:8000'

# ------------Text Processing------------

# request_body = {
#     'text': 'Hi! This is a test text. its purpose is to check functions.',
# }
# response = requests.post(f"{baseUrl}{endpoints.TEXT_PROCESSING}", json = request_body)
# if response.status_code == 200:
#     processed_text = response.json().get('processed_text')
#     print(processed_text)
# else:
#     print(response.status_code)

# ------------PreProcessing------------

docs = datasets.dataset_test_1.docs_iter()
corpus = list(islice(docs, 10))
serialized_corpus = []
for doc in corpus:
    entry = {
        'id': doc.doc_id,
        'text': doc.text,
    }
    serialized_corpus.append(entry)
request_body = {
    'corpus': serialized_corpus
}
response = requests.post(f'{baseUrl}{endpoints.PRE_PROCESSING}', json = request_body)
if response.status_code == 200:
    data = response.json().get('processed_corpus')
    print(data)
else:
    print(response.status_code)