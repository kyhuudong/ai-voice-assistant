from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project_config import setup_app_config
from assistant.assistant_controller import controller as AssistantAudioController

setup_app_config()

app = FastAPI()
controller = APIRouter(prefix='/voice-assistant')
@app.get("/")
def root_route():
    return { "message": "Hello World v3" }

origins = [
    "http://localhost",
    "http://localhost:3000",
    "*"
]

app.include_router(AssistantAudioController, tags=['assistant'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
