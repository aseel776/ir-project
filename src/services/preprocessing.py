import os
from utils.storing import store_dict
from services.text_processing import TextProcessor

class PreProcessor:
    
    def __init__(self, corpus: list[dict], directory: str):
        self.corpus = corpus.copy()
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def start(self):
        processed_corpus = []
        text_processor = TextProcessor()

        for doc in self.corpus:
            processed_text = text_processor.process(doc['text'])
            processed_doc = {
                'id': doc['id'],
                'text': processed_text
            }
            processed_corpus.append(processed_doc)
        store_dict(processed_corpus, f'{self.directory}/processed_corpus.json')
        return processed_corpus
