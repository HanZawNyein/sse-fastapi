from fastapi import Request, APIRouter, Request, Response
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
import os
from utils.log_generator import logGenerator

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/stream-logs')
async def runStatus(request: Request):
    event_generator = logGenerator(request)
    return EventSourceResponse(event_generator)
