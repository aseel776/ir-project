from services.text_processing import process_text, tokenize
from utils.storing import store_pkl, store_npz
from sklearn.feature_extraction.text import TfidfVectorizer

class Indexing:

    def __init__(self, corpus: list[dict], output_dir: str):
        self.corpus = corpus.copy()
        self.output_dir = output_dir

    def start(self):
        docs = [item['text'] for item in self.corpus]

        vectorizer = TfidfVectorizer(preprocessor= process_text, tokenizer= tokenize, token_pattern=None)
        tfidf_matrix = vectorizer.fit_transform(docs)
        
        store_pkl(vectorizer, f'{self.output_dir}/vectorizer.pkl')
        store_npz(tfidf_matrix, f'{self.output_dir}/tf_idf-scikit.npz')
        