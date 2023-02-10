from fastapi import Request, APIRouter
from sse_starlette.sse import EventSourceResponse
from utils.log_generator import logGenerator

router = APIRouter()


@router.get('/stream-logs')
async def runStatus(request: Request):
    event_generator = logGenerator(request)
    return EventSourceResponse(event_generator)
