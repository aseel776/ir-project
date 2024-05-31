from core.endpoints import INDEXING_EP
from services.text_processing import process_text, tokenize
from utils.storing import store_pkl, store_npz
from fastapi import FastAPI, Body
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

@app.post(INDEXING_EP)
async def start(body: dict = Body()):
    print('New request to indexing service !!')
    
    # get params
    corpus = body.get('corpus')
    output_dir = body.get('output_dir')

    # get docs from corpus
    docs = [item['text'] for item in corpus]

    # create index
    vectorizer = TfidfVectorizer(preprocessor= process_text, tokenizer= tokenize, token_pattern=None)
    tfidf_matrix = vectorizer.fit_transform(docs)
    
    # store matrix and model
    store_pkl(vectorizer, f'{output_dir}/vectorizer.pkl')
    store_npz(tfidf_matrix, f'{output_dir}/tf_idf-scikit.npz')