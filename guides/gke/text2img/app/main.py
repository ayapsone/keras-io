from typing import Union

import os
import time
import uuid

import keras_cv
from tensorflow import keras

from PIL import Image

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import uvicorn

app = FastAPI(title="My Own Stable Diffusion API")
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)


class GenerationRequest(BaseModel):
    prompt: str = Field(..., title="Input prompt", description="Input prompt to be rendered")

class GenerationResult(BaseModel):
    download_id: str = Field(..., title="Download ID", description="Identifier to download the generated image")
    time: float = Field(..., title="Time", description="Total duration of generating this image")


@app.get("/")
def home():
        return {"message": "See /docs for documentation"}

#images = model.text_to_image("photograph of an astronaut riding a horse", batch_size=3)
#id = str(uuid.uuid4())

#path = os.path.join("./", f"{id}.png")
#Image.fromarray(images[0]).save(path)

@app.post("/imagine", response_model=GenerationResult)
def generate(req: GenerationRequest):
    start = time.time()
    id = str(uuid.uuid4())
    images = model.text_to_image(req.prompt, batch_size=3)

    path = os.path.join("/app/data", f"{id}.png")
    Image.fromarray(images[0]).save(path)
    elapsed = time.time() - start
    
    return GenerationResult(download_id=id, time=elapsed)

@app.get("/download/{id}", responses={200: {"description": "Image with provided ID", "content": {"image/png" : {"example": "No example available."}}}, 404: {"description": "Image not found"}})
async def download(id: str):
    path = os.path.join("/app/data", f"{id}.png")
    if os.path.exists(path):
        return FileResponse(path, media_type="image/png", filename=path.split(os.path.sep)[-1])
    else:
        raise HTTPException(404, detail="No such file")