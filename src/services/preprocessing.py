from services.text_processing import TextProcessor

class PreProcessor:
    
    def __init__(self, corpus: list[dict]):
        self.corpus = corpus.copy()

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
        
        return processed_corpus
