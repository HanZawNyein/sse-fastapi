from config import settings
from sh import tail


async def logGenerator(request):
    for line in tail("-f", settings.LOGFILE, _iter=True):
        if await request.is_disconnected():
            # print("client disconnected!!!")
            break
        yield line
