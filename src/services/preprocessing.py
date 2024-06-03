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
        from pre_processors import ds1_prep
        structured_corpus = ds1_prep.start()
        
    elif dataset_id == 2:
        from pre_processors import ds2_prep
        structured_corpus = ds2_prep.start()

    elif dataset_id == 3:
        from pre_processors import ds3_prep
        structured_corpus = ds3_prep.start()

    else:
         from pre_processors import ds4_prep
         structured_corpus = ds4_prep.start()

    return {'structured_corpus': structured_corpus}
