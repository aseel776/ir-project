from core.endpoints import INDEXING_EP
from services.text_processing import process_text, tokenize
from utils.storing import store_pkl, store_npz, store_npy
from fastapi import FastAPI, Body
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from transformers import BertModel, BertTokenizer
import torch
import numpy as np

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

    # load pre-trained BERT model and tokenizer
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)

    # get bert embeddings
    encoded_docs = [tokenizer(doc, padding=True, truncation=True, return_tensors='pt') for doc in docs]
    bert_embeddings = np.array([get_bert_embeddings(doc, model) for doc in encoded_docs])
    
    # combine tfidf vectors and bert embeddings
    tfidf_matrix_reshaped = tfidf_matrix.toarray()
    bert_embeddings_reshaped = bert_embeddings.reshape(-1, bert_embeddings.shape[-1])
    combined = np.concatenate((bert_embeddings_reshaped, tfidf_matrix_reshaped), axis=1)

    # K-Means clustering
    clusters_num = get_optimal_clusters_num(combined, 10) 
    kmeans = KMeans(n_clusters = clusters_num, random_state = 33)
    kmeans.fit(combined)
    cluster_labels = kmeans.labels_

    store_pkl(vectorizer, f'{output_dir}/vectorizer.pkl')
    store_npz(tfidf_matrix, f'{output_dir}/tf_idf-scikit.npz')

    store_npy(bert_embeddings, f'{output_dir}/bert_embeddings.npy')

    store_npy(combined, f'{output_dir}/combined.npy')

    store_pkl(kmeans, f'{output_dir}/kmeans.pkl')
    store_npy(np.array(cluster_labels), f'{output_dir}/cluster_labels.npy')

def get_bert_embeddings(encoded_input, model):
        with torch.no_grad():
            output = model(**encoded_input)
        return output.last_hidden_state.mean(dim=1).squeeze().numpy()

def get_optimal_clusters_num(matrix, max_k):
    scores = []

    # silhouette starts at 2 clusters
    k_range = range(2, max_k + 1)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(matrix)
        score = silhouette_score(matrix, kmeans.labels_)
        scores.append((k, score))

    optimal_value = max(scores, key=lambda x: x[1])[0]

    return optimal_value