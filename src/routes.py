from fastapi import FastAPI, Body, APIRouter
from src.services.text_processing import process_text
from src.services.indexing import create_index
from src.services.matching import matach, rank
import src.endpoints as endpoints

router = APIRouter()

@router.post(endpoints.TEXT_PROCESSING)
async def text_processing_endpoint(data: dict = Body()):
    print('tp endpoint')
    text = data.get('text')
    return process_text(text)

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