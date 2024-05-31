from core.endpoints import QUERY_PROCESSING_EP
from utils.loading import load_pkl
from fastapi import FastAPI, Body

app = FastAPI()

@app.post(QUERY_PROCESSING_EP)
async def start(body: dict = Body()):
    print('New request to query_processing service !!')

    # get params
    input_dir = body.get('input_dir')
    query = body.get('query')

    # load vectorizer
    vectorizer = load_pkl(f'{input_dir}/vectorizer.pkl')

    # process
    processed_query = vectorizer.fit([query])
    
    return {'processed_query': processed_query}