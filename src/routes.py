from fastapi import Body, APIRouter
from services.preprocessing import PreProcessor
from services.text_processing import process_text
from services.indexing import Indexing
from services.matching import matach, rank
import endpoints

router = APIRouter()

@router.post(endpoints.PRE_PROCESSING)
async def preprocess_endpoint(body: dict = Body()):
    print('preprocess endpoint')
    dataset_id = body.get('dataset_id')
    output_dir = body.get('output_dir')
    processor = PreProcessor(dataset_id, output_dir)
    structured_corpus = processor.start()
    return {'structured_corpus': structured_corpus}

@router.post(endpoints.TEXT_PROCESSING)
async def text_processing_endpoint(body: dict = Body()):
    print('tp endpoint')
    data = body.get('text')
    processed_text = process_text(text= data)
    return {'processed_text': processed_text}

@router.post(endpoints.INDEXING)
async def indexing_endpoint(body: dict = Body()):
    print('indexing endpoint')
    corpus = body.get('corpus')
    output_dir = body.get('output_dir')
    indexing = Indexing(corpus, output_dir)
    indexing.start()

@router.post(endpoints.MATCHING)
async def matching_endpoint():
    print('matching endpoint')
    return matach()

@router.post(endpoints.RANKING)
async def ranking_endpoint():
    print('ranking endpoint')
    return rank()