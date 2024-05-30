import datasets

def start():

    dataset = datasets.dataset_1
    
    corpus = dataset.docs_iter()

    # ------------ Data Representation ------------

    structured_corpus = []
    for doc in corpus:
        entry = {
            'id': doc.doc_id,
            'text': doc.text,
        }
        structured_corpus.append(entry)

    return structured_corpus
