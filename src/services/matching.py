from core.endpoints import MATCHING_EP
from utils.loading import load_npz
from fastapi import FastAPI, Body
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

@app.post(MATCHING_EP)
async def start(body: dict = Body()):
    print('New request to matching service !!')
    
    # get params
    input_dir = body.get('input_dir')
    processed_query = body.get('processed_query')

    # load matrix
    matrix = load_npz(f'{input_dir}/tf_idf-scikit.npz')

    # measure
    similarities = cosine_similarity(processed_query, matrix).flatten()

    # sort desc (-1) and get top 50
    similar_doc_indices = similarities.argsort()[::-1][:50]

    return {'similar_docs': similar_doc_indices}