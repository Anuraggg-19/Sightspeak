from fastapi import FastAPI
from routers.image_router import router as image_router
import io 
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(image_router , prefix="/api")
@app.get("/")
def read_root():
    return {"message": "Sightspeak's backend is running"}
