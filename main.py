from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes.stream_logs import router as stream_logs_router

# create our app instance
app = FastAPI()

# add CORS so our web page can connect to our api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stream_logs_router)

if __name__ == "__main__":
    # run the app
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
