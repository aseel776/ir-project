import os
from utils.loading import load_df
from database.store_docs import store_docs_in_dataset2

def start():

    # two (..)'s due to 'cwd=os.path.dirname(os.path.abspath(__file__))' in main file
    # which runs servers from project/src
    dataset_path = os.path.join('..', '..', 'Datasets', 'wikIR1k')

    docs_path = os.path.join(dataset_path, 'documents.csv')
    
    docs_df = load_df(docs_path)

    # ------------ Data Representation ------------

    structured_corpus = []

    for _, row in docs_df.iterrows():
        entry = {
            'id': row['id_right'],
            'text': row['text_right'],
        }
        structured_corpus.append(entry)

    store_docs_in_dataset2(structured_corpus)

    return structured_corpus
