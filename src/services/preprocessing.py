import os
from core.endpoints import PRE_PROCESSING_EP
from fastapi import FastAPI, Body

app = FastAPI()

@app.post(PRE_PROCESSING_EP)
async def start(body: dict = Body()):
    print('New request to preprocessing service !!')
    
    # get params
    dataset_id = body.get('dataset_id')
    output_dir = body.get('output_dir')

    # check if output dir does not exist, make one
    if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    # structure dataset
    structured_corpus = []
        
    if dataset_id == 1:        
        import ds1_prep
        structured_corpus = ds1_prep.start()
        
    else:
        import ds2_prep
        structured_corpus = ds2_prep.start()

    return {'structured_corpus': structured_corpus}

