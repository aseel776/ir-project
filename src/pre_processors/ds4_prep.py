import core.datasets as datasets
from database.store_docs import store_docs_in_dataset4

def start():

    dataset = datasets.dataset_test_2
    
    corpus = dataset.docs_iter()

    # ------------ Data Representation ------------

    structured_corpus = []

    for doc in corpus:
        entry = {
            'id': doc.doc_id,            
            'text': doc.text,
        }
        structured_corpus.append(entry)

    store_docs_in_dataset4(structured_corpus)

    return structured_corpus
