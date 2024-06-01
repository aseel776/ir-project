import core.ports as ports
import core.endpoints as endpoints

BASE = 'http://localhost:'

TEXT_PROCESSING_URL = f'{BASE}{ports.TEXT_PROCESSING_PORT}{endpoints.TEXT_PROCESSING_EP}'

PRE_PROCESSING_URL = f'{BASE}{ports.PRE_PROCESSING_PORT}{endpoints.PRE_PROCESSING_EP}'

INDEXING_URL = f'{BASE}{ports.INDEXING_PORT}{endpoints.INDEXING_EP}'

QUERY_PROCESSING_URL = f'{BASE}{ports.QUERY_PROCESSING_PORT}{endpoints.QUERY_PROCESSING_EP}'

MATCHING_URL = f'{BASE}{ports.MATCHING_PORT}{endpoints.MATCHING_EP}'

SEARCHING_URL = f'{BASE}{ports.SEARCHING_PORT}{endpoints.SEARCHING}'