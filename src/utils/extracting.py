def extract_doc_ids(docs: list):
    ids = []

    for doc in docs:
        id = doc['doc_id']        
        ids.append(id)

    return ids
