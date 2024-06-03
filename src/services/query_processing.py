from core.endpoints import QUERY_PROCESSING_EP
from utils.loading import load_pkl
from fastapi import FastAPI, Body
from transformers import BertModel, BertTokenizer
import numpy as np
import torch

app = FastAPI()

@app.post(QUERY_PROCESSING_EP)
async def start(body: dict = Body()):
    print('New request to query_processing service !!')

    # get params
    input_dir = body.get('input_dir')
    query = body.get('query')

    # load vectorizer
    vectorizer = load_pkl(f'{input_dir}/vectorizer.pkl')
    kmeans = load_pkl(f'{input_dir}/kmeans.pkl')

    # process
    processed_query_tfidf = vectorizer.transform([query])

    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)
    encoded_query = tokenizer(query, padding=True, truncation=True, return_tensors='pt')
    processed_query_bert = get_bert_embedding(encoded_query, model)

    processed_query_tfidf_reshaped = processed_query_tfidf.toarray()
    processed_query_bert_reshaped = processed_query_bert.reshape(1, -1)
    combined = np.hstack((processed_query_bert_reshaped, processed_query_tfidf_reshaped))

    # get cluster label
    cluster_label = kmeans.predict(combined)

    print('------------ query processed ------------')
    print(combined)

    # transform it into serializable object
    processed_query_dense = combined.tolist()

    print('------------ query transformed ------------')
    
    return {'processed_query': processed_query_dense, 'cluster_label': int(cluster_label)}

def get_bert_embedding(encoded_input, model):
    with torch.no_grad():
        output = model(**encoded_input)
    return output.last_hidden_state.mean(dim=1).squeeze().numpy()