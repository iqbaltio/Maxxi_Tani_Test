from fastapi import FastAPI
from server.routes import router as TaskRouter

app = FastAPI()

app.include_router(TaskRouter)

@app.get("/")
async def index():
    return "This is Maxxi Tani Test!"