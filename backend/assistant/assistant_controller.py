from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from assistant.assistant_service import handle_audio_from_user

controller = APIRouter(prefix='/')


@controller.get('test', status_code=200)
async def handle_receive_audio_data():
    return { "test": "Hello World v3" }
