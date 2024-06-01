import numpy as np
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
    processed_query_dense = body.get('processed_query')

    print('------------ query recieved ------------')

    # transform it back
    processed_query = np.array(processed_query_dense)

    print('------------ query transformed back ------------')
    print(processed_query)

    # load matrix
    matrix = load_npz(f'{input_dir}/tf_idf-scikit.npz')

    print('------------ matrix loaded ------------')

    # measure
    similarities = cosine_similarity(processed_query, matrix).flatten()

    print('------------ similarities calculated ------------')
    print(similarities)

    # sort desc (-1) and get top 50
    similar_doc_indices = similarities.argsort()[::-1][:5]

    print('------------ similarities sorted ------------')
    print(similar_doc_indices.tolist())


    return {'similar_docs': similar_doc_indices.tolist()}