from fastapi import Body, APIRouter
from services.text_processing import TextProcessor
from services.indexing import create_index
from services.matching import matach, rank
import endpoints

router = APIRouter()

@router.post(endpoints.TEXT_PROCESSING)
async def text_processing_endpoint(body: dict = Body()):
    print('tp endpoint')
    data = body.get('text')
    processor = TextProcessor()
    processor.start_processing(text= data)

@router.post(endpoints.INDEXING)
async def indexing_endpoint(data: dict):
    print('indexing endpoint')
    return create_index(data)

@router.post(endpoints.MATCHING)
async def matching_endpoint():
    print('matching endpoint')
    return matach()

@router.post(endpoints.RANKING)
async def ranking_endpoint():
    print('ranking endpoint')
    return rank()